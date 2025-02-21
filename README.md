Here’s a **README.md** file for your **Credit Worthiness Assessment** project. You can upload this to GitHub as a guide for users.

---

## Credit Worthiness Assessment

### Overview
This project is an **oTree experiment** designed to assess participants' **credit worthiness** based on various personal and financial factors. Participants make financial decisions, provide relevant personal details, and receive a **calculated credit score** and payoff.

### How It Works
The experiment consists of:
1. **Welcome Page** – Introduction to the experiment.
2. **Instructions** – Explanation of the process.
3. **Decision Phase** – Participants decide how much money to give.
4. **Response Phase** – Participants input personal and financial details.
5. **Results Wait Page** – All participants wait for the completion of the experiment.
6. **Results Page** – Final credit score and payoff displayed.

### Credit Score Calculation
The credit score is calculated based on the following factors:

| **Factor**          | **Impact on Credit Score** |
|---------------------|--------------------------|
| Payment History    | +50 points (if good history) |
| Age Group (18-30)  | +20 points |
| Age Group (31-45)  | No change |
| Age Group (46-60)  | -10 points |
| Age Group (61+)    | -20 points |
| Health Insurance   | +30 points (if insured) |
| Dues Payment       | -20 points (if unpaid dues) |
| Marital Status (Married) | +10 points |
| Marital Status (Divorced/Widowed) | -10 points |
| Family Members     | -5 points per additional family member beyond the first one |
| Total Assets       | +1 point per $10,000 in assets |
| Other Income Sources | +15 points |

📌 **Credit score is constrained between 300 and 850.**

### 💰 Payoff Calculation
Final payoff is determined using:
- **Initial Budget**
- **Credit Score / 10**
- **Given Amount**

### Project Motivation
The project aims to address **debt traps** and the **vicious cycle of credit**, which many individuals face due to their **past financial decisions, income levels, and wealth accumulation.** By analyzing these factors, the experiment provides insight into **creditworthiness and responsible borrowing.**

### Installation & Requirements
To run this project, ensure you have **Python** and **oTree** installed. Follow these steps:

```bash
# Install oTree
pip install otree

# Clone the repository
git clone https://github.com/your-repo/credit-worthiness.git

# Navigate to the project folder
cd credit-worthiness

# Start the oTree server
otree devserver
```

Then, access the experiment in your browser at `http://localhost:8000`.

### 👨‍💻 Authors
- **Rythyma Sharma** (Matriculation No.: 3772956)
- **Aditya Sarda** (Matriculation No.: 4730704)


