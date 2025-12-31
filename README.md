# ai-assisted-testgen-sample-python
# Python + Selenium Sample Automation Framework  
*(RAG Test Script Generation POC Dataset)*

This repository contains a minimal, clean Python + Selenium automation framework that will be used as source material for a Retrieval-Augmented Generation (RAG) proof-of-concept.

The goal of this project is not full automation coverage — instead, it provides a small but well-structured reference framework that an AI model can learn patterns from, including:

- Page Objects
- Locator conventions
- Reusable helper methods
- Assertion styles
- Cross-page navigation flows

Future phases will apply a RAG engine + LLM on top of this repository to generate new test scripts that follow the same framework conventions.

---

## 🚀 Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Page Object style helpers

---

## 📁 Project Structure

```
pages/          → Page Object modules
utils/          → driver factory & reusable helpers
tests/          → PyTest test cases
```

Key framework characteristics:

- explicit waits via reusable helper methods  
- clean page interactions (no raw driver calls in tests)  
- simple & readable tests for AI pattern inference  

---

## 🧪 Running Tests

Run from project root:

```bash
python -m pytest
```

Ensure Python and ChromeDriver are installed and on PATH.

---

## 🌐 Target Demo Application

This sample uses the public OrangeHRM demo site:

https://opensource-demo.orangehrmlive.com/

Credentials used in tests:

- Username: `Admin`
- Password: `admin123`

---

## 🧠 RAG POC Background (Why this repo exists)

This repository will later be ingested into a RAG pipeline to enable:

- retrieval of relevant Page Objects & locators
- pattern-aware test script generation
- framework-consistent automation output

The POC objective is to demonstrate:

- reduction in script development effort  
- improvement in first-time execution success  
- pattern-guided framework reuse

---

## 📌 Current Test Scenarios

| Test | Description |
|------|----------|
| `test_login_valid` | Valid login → verify Dashboard loaded |
| `test_navigate_to_my_info` | Login → navigate → verify My Info page |

Additional scenarios will be added gradually to expand learning signals for RAG.

---

## ✔️ Next Planned Milestones

- Build repository ingestion script
- Store embeddings in ChromaDB
- Implement retrieval evaluation tests
- Add prompt-guardrail orchestration
- Integrate with local LLM for POC

---

## 🤝 Contributions / Notes

This repo is intentionally minimal and structured for AI learning clarity — not production-scale automation.

Please follow existing patterns when extending:

- reuse helpers instead of raw driver calls
- follow locator + naming conventions
- keep tests readable and modular

---

## 📄 License

This project is licensed under the **MIT License**.

The intent of this repository is to serve as a sample automation framework
for experimentation and RAG-based AI test-generation research, but the code
may be reused or extended in accordance with the MIT license terms.

See the `LICENSE` file for details.

