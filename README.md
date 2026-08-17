# AI & ML Internship Repository 🚀

Welcome to my internship progress tracker! This repository contains my coding solutions and foundational exercises for AI and Machine Learning.

## 📁 Repository Structure

* 📁 **`python_basics`** - Basic Python code and syntax rules for beginners.
* 📄 **`two_sum.py`** - An optimized $O(n)$ Hash Map solution for LeetCode #1 (Two Sum).

---

## 📌 LeetCode #1: Two Sum (Easy)

### 💡 My Approach: Optimal Hash Map
Instead of checking every pair with two slow loops, this solution uses a **Python Dictionary** to track numbers we have already seen.

1. We loop through the numbers while tracking their position index.
2. We calculate the exact missing number (`diff`) needed to reach our target goal.
3. If the missing number is already in our dictionary, we instantly return the answer!

### 📊 Complexity Analysis
* **Time Complexity:** $O(n)$ — We only look through the list of numbers one time.
* **Space Complexity:** $O(n)$ — In the worst-case scenario, we temporarily store the numbers inside our dictionary map.
