# Current Journal Requirements Ledger — Closeout

Date opened: 2026-09-10  
Current-source refresh: 2026-09-11  
Repository: `ryotamatsuki/standardization-scope-direction-innovation`  
Target journal: *International Journal of Industrial Organization* (IJIO)  
Publisher: Elsevier  
Submission system: Editorial Manager  
Canonical baseline entering the ledger: `main@24f6f357277a8721ff95b12382891c7b69454863`  
Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`  
Workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`

## Final ledger-construction verdict

`LEDGER ESTABLISHED — MATERIAL UNVERIFIED ITEMS RETAINED — AUTHENTICATED PREFLIGHT REQUIRED`

The requirement-ledger construction step is complete. This verdict does **not** mean that every IJIO submission requirement has been verified. The latest workflow requires unresolved material journal-specific rules to remain fail-closed rather than be inferred from publisher defaults, prior submissions, or portal permissiveness.

Canonical artifacts:

- `docs/JOURNAL_REQUIREMENTS_LEDGER.md` — human-readable evidence ledger;
- `docs/JOURNAL_REQUIREMENTS_LEDGER.json` — machine-readable status/blocker summary;
- `tests/test_journal_requirements_ledger.py` — fail-closed regression guard.

## Current-source refresh on 2026-09-11

The following official publisher-wide rules were rechecked and remain current:

1. Elsevier LaTeX instructions state that most journals accept a PDF at initial submission, but journal-specific exceptions and source-file requirements control. When source files are requested, the relevant LaTeX/BibTeX/figure/table/nonstandard dependency files must be bundled as instructed.
2. Elsevier publishing support, updated 2026-08-28, likewise states that most journals accept initial PDF but directs authors to the journal Guide for Authors for journal-specific template/source requirements.
3. Elsevier Highlights guidance requires 3–5 bullets, each no more than 85 characters including spaces, and states that Highlights are not part of editorial consideration and are generally not required until final-files stage unless a journal-specific rule overrides.
4. Elsevier's journal generative-AI policy requires a separate declaration immediately before the references when AI tools are used in manuscript preparation; AI use in the research process should be described in the research/methods documentation. Human authors retain responsibility.
5. Elsevier research-data guidance explicitly uses journal-specific policy options and instructs authors to check the chosen journal's Guide for Authors. Therefore IJIO's exact data-policy option cannot be inferred from publisher-wide guidance.
6. Elsevier artwork guidance accepts/recommends EPS/PDF/TIFF/JPEG, with PDF acceptable for vector artwork. The project's sole policy-regime figure is already a vector PDF with embedded fonts.
7. Elsevier pricing guidance distinguishes optional open-access APCs from subscription publication; authors publishing in hybrid journals can use the subscription route at no publication APC. This does not by itself prove that IJIO has no submission-stage fee or special charge, so the current portal flow remains controlling for that question.

## Journal-specific boundary

The current IJIO official journal page is publicly accessible and verifies the journal identity, ISSN, IO scope, and Elsevier context. The journal-specific ScienceDirect Guide for Authors is identifiable, but its body was not reliably retrievable through the public automated access path used for this audit. The authenticated current IJIO Editorial Manager fields were also not inspected in this chat.

Accordingly the ledger correctly retains material `UNVERIFIED` items including, most importantly:

- current article-type label in the live submission record;
- IJIO's current peer-review/anonymization model;
- whether a separate author title page is required and the exact title-page/manuscript file roles;
- whether PDF-only initial manuscript submission is permitted;
- whether editable Word/LaTeX source is mandatory at initial submission;
- exact source-archive extension/path restrictions if source is required;
- current IJIO abstract/keyword/JEL/template/format rules that are Guide-specific;
- current IJIO research-data policy option and exact data-statement obligation;
- reviewer nomination, subject-area/editor/section, prior-disclosure and other live portal fields;
- any submission-stage payment requirement;
- portal-generated combined PDF and page-by-page final inspection.

These are not defects in the paper. They are submission-rule uncertainties that must be resolved from a higher-level current source.

## Prepared package strengths

The current package is already positioned to satisfy either common branch of the portal rules:

- anonymous review manuscript exists;
- separate author title page exists;
- editable LaTeX/BibTeX source exists;
- exact reproducibility path is established under Stage 9;
- abstract is 167 words;
- six keywords and four JEL codes are prepared;
- four Highlights are prepared and each is below 85 characters;
- vector PDF artwork with embedded fonts exists;
- funding, competing-interest, data-availability, CRediT, and AI declarations are prepared;
- formal-verification and computational-reproducibility artifacts are preserved.

This preparation does not convert any unresolved journal-specific rule into `PASS`.

## Fail-closed downstream contract

The ledger-construction step is closed, but `Stage 14 SUBMISSION QA PASS` remains prohibited while material `UNVERIFIED` items remain.

The authorized route is:

`Current Journal Requirements Ledger ESTABLISHED -> authenticated IJIO Guide / Editorial Manager preflight -> resolve material UNVERIFIED items -> exact source-archive qualification if source is required -> refreshed Stage 14 QA -> new Stage 15 submission freeze`

If authenticated portal access is the only remaining source capable of resolving the outstanding rules, Stage 14 may at most issue `CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED` until those checks are completed.

No theory, theorem, formal certificate, or active freeze changes are authorized by this ledger closeout.
