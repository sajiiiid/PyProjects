from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import count
from math import inf
from typing import Callable, Dict, FrozenSet, Iterable, List, Optional, Set, Tuple


Item = str
Bank = FrozenSet[Item]
State = Tuple[Bank, Bank]

FARMER = "F"
WOLF = "W"
GOAT = "G"
CABBAGE = "C"
ALL_ITEMS = frozenset({FARMER, WOLF, GOAT, CABBAGE})
CARGO = frozenset({WOLF, GOAT, CABBAGE})


@dataclass(frozen=True)
class Action:
    direction: str
    passenger: Optional[Item]

    def label(self) -> str:
        if self.passenger is None:
            return f"Farmer crosses {self.direction} alone"
        return f"Farmer takes {self.passenger} {self.direction}"


@dataclass
class SearchResult:
    algorithm: str
    path: List[State]
    actions: List[Action]
    cost: float
    expanded: int


class FGWCProblem:
    """Farmer, goat, wolf, cabbage problem modeled as a search problem."""

    def __init__(self) -> None:
        self.initial: State = (ALL_ITEMS, frozenset())
        self.goal: State = (frozenset(), ALL_ITEMS)

    def is_goal(self, state: State) -> bool:
        return state == self.goal

    def actions(self, state: State) -> List[Action]:
        left, right = state
        farmer_on_left = FARMER in left
        current_bank = left if farmer_on_left else right
        direction = "right" if farmer_on_left else "left"

        actions = [Action(direction, None)]
        for item in sorted(current_bank - {FARMER}):
            actions.append(Action(direction, item))
        return actions

    def result(self, state: State, action: Action) -> State:
        left, right = state
        moving = {FARMER}
        if action.passenger is not None:
            moving.add(action.passenger)

        moving_bank = frozenset(moving)
        if FARMER in left:
            return left - moving_bank, right | moving_bank
        return left | moving_bank, right - moving_bank

    def is_valid(self, state: State) -> bool:
        left, right = state
        return self._bank_is_valid(left) and self._bank_is_valid(right)

    def step_cost(self, _state: State, _action: Action, _next_state: State) -> float:
        return 1.0

    def heuristic(self, state: State) -> float:
        left, _right = state
        return float(len(left & CARGO))

    @staticmethod
    def _bank_is_valid(bank: Bank) -> bool:
        if FARMER in bank:
            return True
        if GOAT in bank and WOLF in bank:
            return False
        if GOAT in bank and CABBAGE in bank:
            return False
        return True


def successors(problem: FGWCProblem, state: State) -> Iterable[Tuple[Action, State, float]]:
    for action in problem.actions(state):
        next_state = problem.result(state, action)
        if problem.is_valid(next_state):
            yield action, next_state, problem.step_cost(state, action, next_state)


def reconstruct_result(
    algorithm: str,
    problem: FGWCProblem,
    parent: Dict[State, Tuple[Optional[State], Optional[Action]]],
    goal: State,
    cost: float,
    expanded: int,
) -> SearchResult:
    path = [goal]
    actions: List[Action] = []
    state = goal

    while state != problem.initial:
        previous_state, action = parent[state]
        if previous_state is None or action is None:
            break
        path.append(previous_state)
        actions.append(action)
        state = previous_state

    path.reverse()
    actions.reverse()
    return SearchResult(algorithm, path, actions, cost, expanded)


def breadth_first_search(problem: FGWCProblem) -> SearchResult:
    frontier = deque([problem.initial])
    parent: Dict[State, Tuple[Optional[State], Optional[Action]]] = {
        problem.initial: (None, None)
    }
    expanded = 0

    while frontier:
        state = frontier.popleft()
        expanded += 1

        if problem.is_goal(state):
            return reconstruct_result(
                "BFS", problem, parent, state, len(parent_path(parent, state)) - 1, expanded
            )

        for action, next_state, _cost in successors(problem, state):
            if next_state not in parent:
                parent[next_state] = (state, action)
                frontier.append(next_state)

    return SearchResult("BFS", [], [], inf, expanded)


def depth_first_search(problem: FGWCProblem) -> SearchResult:
    frontier = [problem.initial]
    parent: Dict[State, Tuple[Optional[State], Optional[Action]]] = {
        problem.initial: (None, None)
    }
    explored: Set[State] = set()
    expanded = 0

    while frontier:
        state = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        expanded += 1

        if problem.is_goal(state):
            return reconstruct_result(
                "DFS", problem, parent, state, len(parent_path(parent, state)) - 1, expanded
            )

        for action, next_state, _cost in reversed(list(successors(problem, state))):
            if next_state not in explored and next_state not in parent:
                parent[next_state] = (state, action)
                frontier.append(next_state)

    return SearchResult("DFS", [], [], inf, expanded)


def uniform_cost_search(problem: FGWCProblem) -> SearchResult:
    return priority_search(problem, "UCS", priority=lambda path_cost, _state: path_cost)


def a_star_search(problem: FGWCProblem) -> SearchResult:
    return priority_search(
        problem,
        "A*",
        priority=lambda path_cost, state: path_cost + problem.heuristic(state),
    )


def priority_search(
    problem: FGWCProblem,
    algorithm: str,
    priority: Callable[[float, State], float],
) -> SearchResult:
    tie_breaker = count()
    frontier: List[Tuple[float, int, float, State]] = []
    heappush(frontier, (priority(0.0, problem.initial), next(tie_breaker), 0.0, problem.initial))

    parent: Dict[State, Tuple[Optional[State], Optional[Action]]] = {
        problem.initial: (None, None)
    }
    best_cost: Dict[State, float] = {problem.initial: 0.0}
    expanded = 0

    while frontier:
        _priority, _order, path_cost, state = heappop(frontier)
        if path_cost > best_cost.get(state, inf):
            continue

        expanded += 1
        if problem.is_goal(state):
            return reconstruct_result(algorithm, problem, parent, state, path_cost, expanded)

        for action, next_state, step_cost in successors(problem, state):
            new_cost = path_cost + step_cost
            if new_cost < best_cost.get(next_state, inf):
                best_cost[next_state] = new_cost
                parent[next_state] = (state, action)
                heappush(
                    frontier,
                    (
                        priority(new_cost, next_state),
                        next(tie_breaker),
                        new_cost,
                        next_state,
                    ),
                )

    return SearchResult(algorithm, [], [], inf, expanded)


def backtracking_search(problem: FGWCProblem) -> SearchResult:
    best_path: Optional[List[State]] = None
    best_actions: Optional[List[Action]] = None
    expanded = 0

    def backtrack(
        state: State,
        path: List[State],
        actions: List[Action],
        visited: Set[State],
    ) -> None:
        nonlocal best_path, best_actions, expanded
        expanded += 1

        if problem.is_goal(state):
            if best_path is None or len(path) < len(best_path):
                best_path = path.copy()
                best_actions = actions.copy()
            return

        if best_path is not None and len(path) >= len(best_path):
            return

        for action, next_state, _cost in successors(problem, state):
            if next_state in visited:
                continue
            visited.add(next_state)
            path.append(next_state)
            actions.append(action)
            backtrack(next_state, path, actions, visited)
            actions.pop()
            path.pop()
            visited.remove(next_state)

    backtrack(problem.initial, [problem.initial], [], {problem.initial})

    if best_path is None or best_actions is None:
        return SearchResult("Backtracking", [], [], inf, expanded)
    return SearchResult(
        "Backtracking",
        best_path,
        best_actions,
        float(len(best_actions)),
        expanded,
    )


def parent_path(
    parent: Dict[State, Tuple[Optional[State], Optional[Action]]], goal: State
) -> List[State]:
    path = [goal]
    state = goal
    while parent[state][0] is not None:
        state = parent[state][0]  # type: ignore[assignment]
        path.append(state)
    path.reverse()
    return path


def format_state(state: State) -> str:
    left, right = state
    return f"Left={format_bank(left):12} | Right={format_bank(right):12}"


def format_bank(bank: Bank) -> str:
    ordered = [item for item in [FARMER, WOLF, GOAT, CABBAGE] if item in bank]
    return "{" + ",".join(ordered) + "}"


def print_result(result: SearchResult) -> None:
    print(f"\n{result.algorithm}")
    print("-" * len(result.algorithm))

    if not result.path:
        print("No solution found.")
        return

    print(f"Cost: {result.cost:g}")
    print(f"Expanded states: {result.expanded}")
    print("Path:")
    print(f"  0. {format_state(result.path[0])}")
    for index, action in enumerate(result.actions, start=1):
        print(f"     -> {action.label()}")
        print(f"  {index}. {format_state(result.path[index])}")


def main() -> None:
    problem = FGWCProblem()
    searches = [
        breadth_first_search,
        depth_first_search,
        uniform_cost_search,
        a_star_search,
        backtracking_search,
    ]

    for search in searches:
        print_result(search(problem))


if __name__ == "__main__":
    main()
