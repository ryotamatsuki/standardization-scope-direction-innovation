# IJIO Authenticated Guide / Editorial Manager Preflight

Date: 2026-09-11

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Canonical baseline entering preflight: `main@12140b079fa315d012b07d8ec45d3c7130863b7f`

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Target journal: *International Journal of Industrial Organization* (IJIO)

Submission system: Editorial Manager

## Verdict

`CONDITIONAL PASS — AUTHENTICATED PORTAL OBSERVATION REQUIRED`

The preflight design and all non-authenticated checks are complete. The remaining material questions are specific to the current authenticated IJIO submission flow and cannot be closed from publisher-wide defaults, indexed snippets, or a different manuscript's prior submission record.

This is not a paper defect and does not trigger theory or manuscript rollback. It is a submission-interface evidence boundary.

## Evidence completed before portal observation

Current official Elsevier guidance was refreshed on 2026-09-11. The following publisher-wide facts are confirmed but are not promoted to IJIO-specific rules where the journal configuration controls:

- Elsevier states that most journals accept PDF at initial submission, while journal-specific exceptions and source-file requirements control.
- For journals using double-anonymized review, Elsevier requires a separate title page and anonymized manuscript; IJIO's current use of that review model remains a journal-specific portal/Guide question.
- Elsevier research-data requirements vary by journal policy option; the target journal's Guide or submission flow must be checked.
- Elsevier submission flows may expose data-statement questions directly in the submission process.
- Editorial Manager submission steps vary by publication configuration and article type; publication-specific instructions therefore control.

Recent actual IJIO operational history in the author's account is retained only as non-authoritative supporting evidence: a 2026-09-05 IJIO submission confirmation used the article-type label `Research Paper`, and a 2026-09-08 IJIO system message confirmed that the submission PDF was built and required author approval. These facts make the expected workflow plausible but do not certify the current submission record for this manuscript.

## Authenticated observation contract

The current IJIO submission record must be inspected and the following items recorded exactly as shown. Screenshots or copied field labels are acceptable evidence; memory or inference is not.

| ID | Required observation | Close condition |
|---|---|---|
| AP01 | Log in to IJIO and open/create the current submission record for this manuscript | Current IJIO record visibly open under the author's account |
| AP02 | Article type | Current dropdown/selection confirms the applicable type, expected historical value `Research Paper` |
| AP03 | Peer-review/anonymity instructions | Current IJIO instructions explicitly establish single- vs double-anonymized handling and any identity-removal rule |
| AP04 | Required file-designation options | All current mandatory file item types are enumerated |
| AP05 | PDF-only vs editable source at initial submission | Current Guide/portal states whether anonymous manuscript PDF suffices initially and whether LaTeX source is mandatory now |
| AP06 | Title page and figure handling | Current file roles establish separate title-page and separate/embedded figure requirements |
| AP07 | Abstract / keyword / JEL / format fields | Exact required fields and current limits are recorded |
| AP08 | Reviewer nominations | Exact minimum/maximum/optional requirement is recorded |
| AP09 | Data / code / preprint / AI / declarations / attestations | Every mandatory submission question and response set is recorded |
| AP10 | Submission-stage payment | Current flow confirms whether any mandatory payment is required before submission |
| AP11 | Editorial Manager generated submission PDF | PDF build completes for this manuscript |
| AP12 | Page-by-page generated-PDF inspection | Anonymity, equations, figure, references, appendix, metadata, and ordering all pass visual inspection |
| AP13 | Final file inventory | No missing, duplicated, stale, or misdesignated file remains immediately before Submit |

## Portal capture template

For each AP item, record:

- current screen/page name;
- exact field or instruction text;
- required/optional status;
- selected value;
- affected repository file;
- evidence type (`PORTAL_SCREEN`, `CURRENT_GUIDE`, or `DIRECT_EDITORIAL_INSTRUCTION`);
- date/time observed;
- resulting ledger requirement IDs closed.

Do not record passwords, authentication tokens, recovery codes, or other secrets in the repository.

## Expected file mapping to test in the portal

The package is prepared for either common initial-submission branch:

- anonymous manuscript: `paper/main.pdf`;
- separate title page: `submission/ijio_title_page.pdf`;
- Highlights: `submission/ijio_highlights.txt`;
- cover letter: `submission/ijio_cover_letter.md` as source text for paste/upload as required;
- declarations/metadata: `submission/ijio_declarations.md`, `submission/ijio_submission_metadata.md` as source records;
- figure: `figures/policy_regime_map.pdf` if a separate artwork item is required;
- editable source: `paper/`, `references/references.bib`, and required figure dependencies if current IJIO requires source at initial submission.

No source archive should be frozen until AP05/AP06 establish the actual upload contract. If editable source is required, refreshed Stage 14 must create and clean-build the exact upload archive, inspect its contents, and verify that the rebuilt PDF matches the intended manuscript.

## Fail-closed routing

Full `SUBMISSION QA PASS` is not authorized while any material current-portal item above remains unresolved.

If all non-portal QA passes but authenticated observations are still missing, the maximum permissible state remains:

`CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED`

Once AP01–AP13 are evidenced, update `docs/JOURNAL_REQUIREMENTS_LEDGER.md` and `.json` requirement-by-requirement. Only then proceed to refreshed Stage 14 full QA; if source upload is required, perform exact source-archive qualification first.

Authorized route:

`authenticated portal observation -> reconcile Journal Requirements Ledger -> exact source-archive qualification if required -> refreshed Stage 14 QA -> new Stage 15 submission freeze`

Scientific delta: `NONE`.
