Planning
========

Rationale, ruminations, rewriting, racheting, rational..

Workflow
--------

- ir should be dumpable & diffable
- debug logging should be able to dump ir in between 
    passes so we can incrementally debug the passes
- transforms / passes should distinct from coder
- but coder can spec required passes 
- need a graph-subgarph isomorphism test (matching)?

- three phases of transforms
  - simulator primitives translate themselves to ir
  - various transforms for optimization?
  - pre-coder transforms required 
- then coder generates actual code

- what about runtime & allocation?


