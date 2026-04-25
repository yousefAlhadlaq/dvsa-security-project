# ICS-344 DVSA Security Project

> **Course:** ICS-344 — Information Security | Section 1  
> **Institution:** King Fahd University of Petroleum and Minerals  
> **Term:** 252 — Spring 2026

---

## 👥 Team

| Student Name      | Student ID | Lessons Assigned         |
| ----------------- | ---------- | ------------------------ |
| Yousef Alhadlaq   | 202274280  | Lessons 1, 2, 8, 10, B1  |
| Abdulellah Alamer | 202265520  | Lessons 4, 6, B2, B3, B4 |
| Faris Alshahrany  | 202277660  | Lessons 3, 5, 7, 9, B5   |

---

## 🌐 Deployment Info

| Field            | Value                                                                          |
| ---------------- | ------------------------------------------------------------------------------ |
| DVSA Website URL | http://dvsa-website-786427517680-us-east-1.s3-website.us-east-1.amazonaws.com/ |
| AWS Region       | us-east-1                                                                      |
| Submission Date  | 26 April 2026                                                                  |

---

## 📹 Vulnerability Recordings

All demonstration recordings (exploit + fix verification) are available in the shared folder below:

🔗 **[📂 Open Recordings Folder](https://kfupmedusa-my.sharepoint.com/:f:/r/personal/s202274280_kfupm_edu_sa/Documents/ICS344/project/recording?csf=1&web=1&e=m9rlOy)**

> Each recording covers the full demonstration: exploit walkthrough, evidence collection, fix applied, and post-fix verification.

---

## 🔐 Vulnerability Lessons

| #   | Vulnerability                         | Assigned To | Status      |
| --- | ------------------------------------- | ----------- | ----------- |
| 01  | Event Injection                       | Yousef      | ✅ Complete |
| 02  | Broken Authentication                 | Yousef      | ✅ Complete |
| 03  | Sensitive Data Exposure               | Faris       | ✅ Complete |
| 04  | XML External Entities (XXE)           | Abdulellah  | ✅ Complete |
| 05  | Broken Access Control                 | Faris       | ✅ Complete |
| 06  | Security Misconfiguration             | Abdulellah  | ✅ Complete |
| 07  | Over-Privileged Function              | Faris       | ✅ Complete |
| 08  | Logic Vulnerabilities                 | Yousef      | ✅ Complete |
| 09  | Components with Known Vulnerabilities | Faris       | ✅ Complete |
| 10  | Insufficient Logging & Monitoring     | Yousef      | ✅ Complete |
| B1  | Bonus Finding 1                       | Yousef      | ✅ Complete |
| B2  | Bonus Finding 2                       | Abdulellah  | ✅ Complete |
| B3  | Bonus Finding 3                       | Abdulellah  | ✅ Complete |
| B4  | Bonus Finding 4                       | Abdulellah  | ✅ Complete |
| B5  | Bonus Finding 5                       | Faris       | ✅ Complete |

---

## 🗂️ Repository Structure

```text
dvsa-security-project/
├── README.md                        # Project overview, team info, and lesson index
├── report/                          # Final written report artifacts
├── slides/                          # Presentation slides
├── demo/                            # Demo files or local recording copies
└── vulnerabilities/
    └── lesson-XX-name/
        ├── exploit/                 # Exploit payloads and proof-of-concept scripts
        ├── fix/                     # Before and after patched code or config files
        └── screenshots/             # Evidence screenshots for each phase
```

Each `vulnerabilities/lesson-XX/README.md` follows the 10-section project template:

1. Goal and Vulnerability Summary
2. Why This Works / Root Cause
3. Environment and Setup
4. Reproduction Steps
5. Evidence and Proof
6. Fix Strategy / Probable Mitigation
7. Code / Config Changes
8. Verification After Fix
9. Structured Analysis (Table A + Table B)
10. Takeaway / Lessons Learned

---

## ⚠️ Disclaimer

This project is strictly for educational purposes within ICS-344 at KFUPM (Term 252).  
DVSA is deployed in a non-production AWS account. All techniques demonstrated are legal within this controlled classroom environment.  
Unauthorized use or reproduction of this material outside this course is strictly prohibited.
