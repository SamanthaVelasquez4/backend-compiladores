
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CANTIDAD FIN MONEDAinstruccion : CANTIDAD MONEDA MONEDA FIN'
    
_lr_action_items = {'CANTIDAD':([0,],[2,]),'$end':([1,5,],[0,-1,]),'MONEDA':([2,3,],[3,4,]),'FIN':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instruccion':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instruccion","S'",1,None,None,None),
  ('instruccion -> CANTIDAD MONEDA MONEDA FIN','instruccion',4,'p_instruccion','analizador_sintactico.py',6),
]
