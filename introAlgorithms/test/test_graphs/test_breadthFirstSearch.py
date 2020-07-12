import os, sys
sys.path.insert (0, os.path.abspath ('./'))

import pytest
from graphs.breadthFirstSearch import bfs, create_nodes, shortest_path

@pytest.mark.skip
def test_bfs ():
	s,r,v,w,t,x,u,y = create_nodes (8)
	s.connect (r)
	s.connect (w)
	r.connect (v)
	w.connect (t)
	w.connect (x)
	t.connect (x)
	t.connect (u)
	x.connect (y)
	x.connect (u)
	u.connect (y)

	bfs (s)

	assert s.parent () is None
	assert r.parent () is s and w.parent () is s
	assert r.distance () == w.distance () and r.distance () == 1
	assert v.parent () is r and v.distance () == 2
	assert t.parent () is w and x.parent () is w
	assert t.distance () == x.distance () and x.distance () == 2
	assert u.parent () is t and y.parent () is x
	assert u.distance () == y.distance () and u.distance () == 3

# @pytest.mark.skip
def test_shortest_path ():
	s,r,v,w,t,x,u,y = create_nodes (8)
	s.connect (r)
	s.connect (w)
	r.connect (v)
	w.connect (t)
	w.connect (x)
	t.connect (x)
	t.connect (u)
	x.connect (y)
	x.connect (u)
	u.connect (y)

	bfs (s)
	p = shortest_path (s, u)
	exp_p = [s, w, t, u]
	
	assert len (p) == len (exp_p)
	for i in range (len (p)):
		assert p[i] == exp_p[i]



