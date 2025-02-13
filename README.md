---

# 📊 **Exploratory Data Analysis (EDA) on OLX Mobile Phone Dataset**  

## **📌 Project Overview**  
This project performs **Exploratory Data Analysis (EDA)** on an **OLX mobile phone dataset** to gain insights into the availability, conditions, and popularity of different mobile brands. The analysis includes **data cleaning, visualization, and statistical exploration** to understand trends in the second-hand mobile market.  

---

## **📂 Dataset Description**  
The dataset contains information about various mobile phones listed on OLX, including:  

📌 **Brand** – The mobile phone brand (e.g., Apple, Samsung, Xiaomi).  
📌 **Total** – The total number of listings for each brand.  
📌 **Used** – The number of used phones available.  
📌 **New** – The number of new phones available.  
📌 **Open-Box** – Phones that are new but unsealed.  
📌 **For Parts** – Phones sold for parts or repairs.  
📌 **Refurbished** – Phones that have been restored or repaired for resale.  

---

## **🛠️ Requirements**  

### **📌 Libraries Used**  
Ensure you have the following Python libraries installed before running the code:  
```bash
pip install pandas numpy matplotlib seaborn
```

---

## **📊 Exploratory Data Analysis (EDA) Steps**  

### **1️⃣ Data Cleaning & Preprocessing**  
✅ Load the dataset and remove duplicates.  
✅ Standardize column names (convert to lowercase, strip spaces).  
✅ Check for missing values and handle them if necessary.  

### **2️⃣ Summary Statistics**  
✅ Display dataset structure and first few rows.  
✅ Count unique brands and phone conditions.  

### **3️⃣ Data Visualization**  
📌 **Top 10 Mobile Brands** – Bar chart showing brands with the most listings.  
📌 **Condition Distribution** – Bar chart comparing "Used," "New," "Open-Box," "For Parts," and "Refurbished" phones.  
📌 **Correlation Heatmap** – Shows relationships between different phone conditions.  
📌 **Box Plot for Outlier Detection** – Identifies extreme values in phone conditions.  

---

## **📈 Expected Insights**  
🔹 Which brand has the highest and lowest total listings?  
🔹 How many phones are in "Used," "New," and "For Parts" conditions?  
🔹 Is there a correlation between "Used" and "New" phone availability?  
🔹 Are there any extreme values (outliers) in the dataset?  

---

## **🚀 How to Run the Code**  

### **1️⃣ Clone the Repository (Optional)**  
```bash
git clone https://github.com/your-repo/olx-mobile-eda.git
cd olx-mobile-eda
```

### **2️⃣ Run the Python Script**  
```bash
olx_eda_script.py
```

### **3️⃣ Check the Outputs**  
✅ The script will display **insights in the terminal**.  
✅ **Graphs and plots** will open for better visualization.  

---

## **📬 Contact & Contributions**  
Feel free to contribute by improving data visualizations or adding more analyses!  

🔗 **LinkedIn:** [Muhammad Ahmad](https://www.linkedin.com/in/muhammad-ahmad-137b36241/)  

---

### **🔹 Happy Analyzing! 🚀📊**  
