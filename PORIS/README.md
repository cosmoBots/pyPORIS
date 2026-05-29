# PORIS Python Runtime

This directory contains the Python runtime used by generated PORIS models.

The current toolchain generates Python model classes under `output/py/...` and
executes them with this directory in `PYTHONPATH`. Those generated models import
the runtime classes from here, instantiate the PORIS tree, and can export the
model to XML through `toXML()`.

## Contents

```text
PORIS.py
```

Main Python runtime currently used by the generated `*PORIS.py` files. It
contains the PORIS node classes, XML import/export support, value/mode/system
relationships, formatter support, and command-node behavior.

```text
MVC/
```

Alternative Python implementation organized around MVC-style base classes,
models, views, controllers, observers and formatter classes. It is not yet the
default runtime for generated user models, but it is an important reference for
the planned consolidation of the Python implementations.

```text
$S1_physical/
```

Template for the editable physical companion generated next to each Python
model. The generated automatic model should be treated as disposable; the
physical companion is where user-specific execution logic belongs.

## Runtime Role

The usual generation chain is:

```text
GraphML -> generated Python model -> PORIS runtime -> XML
```

The Java Swing panel consumes the XML. The Python runtime is therefore the
central representation layer for the model after parsing.

Keeping the runtime stable is important because several products depend on it:

- XML generated from Python for `AstroPorisPlayer`
- executable Python physical models
- future optional products generated from the same model tree

## Command Nodes

PORIS command nodes are represented as callable Python behavior on the owning
system. If a command has no custom implementation, the default behavior prints an
execution trace. User code can override or register behavior in the physical
companion.

## Import Path

Scripts such as `porispanel.sh`, `doPorisPython.sh` and `runPorisModel.sh` add
this directory to `PYTHONPATH`, so generated models can import `PORIS.py`
without copying or symlinking the runtime into generated output folders.

## Direction

The repository currently contains two Python runtime lines: this default
`PORIS.py` implementation and the `MVC/` implementation. The long-term goal is
to keep a single Python runtime that combines the production features of the
default runtime with the cleaner foundations of the MVC implementation.

The sibling submodules `cxxPORIS` and `rbPORIS` provide C++ and Ruby runtimes
and code generators. They are expected to become optional products driven by the
same model-generation scripts.
