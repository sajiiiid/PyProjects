from __future__ import annotations

from heapq import heappop, heappush
from itertools import count
from math import inf
from typing import Dict, Hashable, List, Tuple


Graph = Dict[Hashable, List[Tuple[Hashable, float]]]


def reconstruct_path(
	parent: Dict[Hashable, Hashable], start: Hashable, goal: Hashable
) -> List[Hashable]:
	"""Rebuild the path from start to goal using parent links."""
	path = [goal]
	node = goal
	while node != start:
		node = parent[node]
		path.append(node)
	path.reverse()
	return path


def uniform_cost_search(
	graph: Graph, start: Hashable, goal: Hashable
) -> Tuple[float, List[Hashable]]:
	"""
	Uniform Cost Search (Dijkstra-style for non-negative edges).

	Returns:
		(best_cost, path)
		- best_cost is ``inf`` and path is [] if goal is unreachable.
	"""
	if start == goal:
		return 0.0, [start]

	frontier = []
	tie_breaker = count()
	heappush(frontier, (0.0, next(tie_breaker), start))

	best_cost: Dict[Hashable, float] = {start: 0.0}
	parent: Dict[Hashable, Hashable] = {}
	explored = set()

	while frontier:
		current_cost, _, state = heappop(frontier)

		# Skip stale entries and already-expanded states.
		if state in explored or current_cost > best_cost.get(state, inf):
			continue

		if state == goal:
			return current_cost, reconstruct_path(parent, start, goal)

		explored.add(state)

		for successor, edge_cost in graph.get(state, []):
			if successor in explored:
				continue

			new_cost = current_cost + edge_cost
			if new_cost < best_cost.get(successor, inf):
				best_cost[successor] = new_cost
				parent[successor] = state
				heappush(frontier, (new_cost, next(tie_breaker), successor))

	return inf, []


def _run_demo_tests() -> None:
	graph: Graph = {
		"A": [("B", 1), ("C", 4)],
		"B": [("D", 2), ("E", 7)],
		"C": [("D", 1)],
		"D": [("F", 3)],
		"E": [("F", 1)],
		"F": [],
		"X": [],
	}

	cost, path = uniform_cost_search(graph, "A", "F")
	assert cost == 6.0
	assert path == ["A", "B", "D", "F"]

	unreachable_cost, unreachable_path = uniform_cost_search(graph, "A", "X")
	assert unreachable_cost == inf
	assert unreachable_path == []

	print("UCS demo passed.")
	print(f"Best path A -> F: {' -> '.join(path)} (cost={cost})")


if __name__ == "__main__":
	_run_demo_tests()

