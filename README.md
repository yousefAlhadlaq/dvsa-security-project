# DVSA Security Project

| Field          | Value          |
|----------------|----------------|
| Course         | ___________________ |
| Student Names  | ___________________ |
| Student IDs    | ___________________ |
| DVSA URL       | ___________________ |
| AWS Region     | ___________________ |
| Date           | ___________________ |

---

## Lessons

| # | Vulnerability | Status |
|---|---------------|--------|
| 01 | Event Injection | Not Started |
| 02 | Broken Authentication | Not Started |
| 03 | [Vulnerability Name] | Not Started |
| 04 | [Vulnerability Name] | Not Started |
| 05 | [Vulnerability Name] | Not Started |
| 06 | [Vulnerability Name] | Not Started |
| 07 | Overprivileged Function | Not Started |
| 08 | [Vulnerability Name] | Not Started |
| 09 | [Vulnerability Name] | Not Started |
| 10 | [Vulnerability Name] | Not Started |

---

## How to Navigate This Repo

```
.
├── README.md                  # This file — project overview and lesson index
├── report/                    # Final written report artifacts
├── slides/                    # Presentation slides
├── scripts/                   # Automation or helper scripts
├── demo/                      # Demo files or recordings
└── vulnerabilities/
    └── lesson-XX[-name]/
        ├── README.md          # Full write-up for this lesson (10-section template)
        ├── exploit/           # Exploit code, payloads, or PoC scripts
        ├── fix/               # Patched code or config files
        └── screenshots/       # Evidence screenshots
```

Each `vulnerabilities/lesson-XX/README.md` follows a 10-section template:

1. Goal and Vulnerability Summary
2. Why This Works / Root Cause
3. Environment and Setup
4. Reproduction Steps
5. Evidence and Proof
6. Fix Strategy / Probable Mitigation
7. Code / Config Changes
8. Verification After Fix
9. Structured Operation and Security Analysis (two tables)
10. Takeaway / Lessons Learned
