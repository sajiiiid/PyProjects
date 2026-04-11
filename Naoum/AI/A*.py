from heapq import heappop, heappush
from itertools import count
from math import inf
from typing import Callable, Dict, Hashable, List, Tuple


Graph = Dict[Hashable, List[Tuple[Hashable, float]]]
Heuristic = Callable[[Hashable, Hashable], float]


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


def a_star_search(
	graph: Graph, start: Hashable, goal: Hashable, heuristic: Heuristic
) -> Tuple[float, List[Hashable]]:
	"""
	A* search for weighted graphs with non-negative edge costs.

	Returns:
		(best_cost, path)
		- best_cost is ``inf`` and path is [] if goal is unreachable.
	"""
	if start == goal:
		return 0.0, [start]

	frontier = []
	tie_breaker = count()
	heappush(frontier, (float(heuristic(start, goal)), 0.0, next(tie_breaker), start))

	best_cost: Dict[Hashable, float] = {start: 0.0}
	parent: Dict[Hashable, Hashable] = {}

	while frontier:
		_, g_score, _, node = heappop(frontier)

		# Skip outdated queue entries.
		if g_score > best_cost.get(node, inf):
			continue

		if node == goal:
			return g_score, reconstruct_path(parent, start, goal)

		for successor, edge_cost in graph.get(node, []):
			if edge_cost < 0:
				raise ValueError("A* requires non-negative edge costs.")

			new_g = g_score + edge_cost
			if new_g < best_cost.get(successor, inf):
				best_cost[successor] = new_g
				parent[successor] = node
				h_score = float(heuristic(successor, goal))
				heappush(
					frontier,
					(new_g + h_score, new_g, next(tie_breaker), successor),
				)

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

	heuristics: Dict[Hashable, float] = {
		"A": 5.0,
		"B": 4.0,
		"C": 3.0,
		"D": 2.0,
		"E": 1.0,
		"F": 0.0,
		"X": 0.0,
	}

	def h(node: Hashable, _: Hashable) -> float:
		return heuristics.get(node, 0.0)

	cost, path = a_star_search(graph, "A", "F", h)
	assert cost == 6.0
	assert path == ["A", "B", "D", "F"]

	unreachable_cost, unreachable_path = a_star_search(graph, "A", "X", h)
	assert unreachable_cost == inf
	assert unreachable_path == []

	print("A* demo passed.")
	print(f"Best path A -> F: {' -> '.join(map(str, path))} (cost={cost})")


if __name__ == "__main__":
	_run_demo_tests()

