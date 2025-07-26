import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import time
import re

# Configure page
st.set_page_config(
    page_title="SQL Optimizer Suite",
    page_icon="🗃️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 2px solid #1f77b4;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #28a745;
    }
    .warning-card {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .success-card {
        background: #d4edda;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🗃️ SQL Optimizer Suite")
st.sidebar.markdown("---")

pages = {
    "🏠 Dashboard": "dashboard",
    "💬 Natural Language to SQL": "nl_to_sql",
    "⚡ Query Performance Analyzer": "performance_analyzer",
    "📊 Index Advisor": "index_advisor",
    "📖 Query Plan Explainer": "plan_explainer",
    "🔍 SQL Code Reviewer": "code_reviewer",
    "📈 Regression Detector": "regression_detector",
    "📚 Demo Examples": "demo_examples"
}

selected_page = st.sidebar.selectbox("Select Tool", list(pages.keys()))

# Main content based on selected page
if pages[selected_page] == "dashboard":
    st.markdown('<div class="main-header">SQL Query & Performance Optimization Suite</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Welcome to the comprehensive SQL optimization platform powered by AI. This suite provides intelligent 
    database performance optimization tools to help you write better queries, identify bottlenecks, 
    and maintain optimal database performance.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>1,247</h3>
            <p>Queries Optimized</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>89%</h3>
            <p>Avg Performance Gain</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>342</h3>
            <p>Indexes Recommended</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>23</h3>
            <p>Regressions Detected</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Available Tools")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>💬 Natural Language to SQL</h4>
            <p>Convert plain English requests into optimized SQL queries using advanced language models.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>⚡ Performance Analyzer</h4>
            <p>AI-powered analysis of slow queries with specific optimization recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Index Advisor</h4>
            <p>ML-based recommendations for optimal index creation and removal strategies.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📖 Query Plan Explainer</h4>
            <p>Natural language explanations of complex database execution plans.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 SQL Code Reviewer</h4>
            <p>Automated code review for SQL scripts and stored procedures with best practices.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📈 Regression Detector</h4>
            <p>Monitor and identify when queries start performing poorly over time.</p>
        </div>
        """, unsafe_allow_html=True)

elif pages[selected_page] == "nl_to_sql":
    st.title("💬 Natural Language to SQL Converter")
    st.markdown("Convert your natural language requests into optimized SQL queries.")
    
    # Sample schemas for demo
    schemas = {
        "E-commerce": {
            "users": ["user_id", "username", "email", "created_at", "status"],
            "orders": ["order_id", "user_id", "total_amount", "order_date", "status"],
            "products": ["product_id", "name", "price", "category_id", "stock_quantity"],
            "order_items": ["order_id", "product_id", "quantity", "unit_price"]
        },
        "HR System": {
            "employees": ["employee_id", "first_name", "last_name", "department_id", "salary", "hire_date"],
            "departments": ["department_id", "department_name", "manager_id"],
            "projects": ["project_id", "project_name", "start_date", "end_date", "budget"]
        }
    }
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        selected_schema = st.selectbox("Select Database Schema", list(schemas.keys()))
        
        st.subheader("Available Tables")
        for table, columns in schemas[selected_schema].items():
            with st.expander(f"📋 {table}"):
                st.write("Columns:", ", ".join(columns))
    
    with col2:
        st.subheader("Natural Language Query")
        nl_query = st.text_area(
            "Describe what you want to query:",
            placeholder="e.g., Show me the top 5 customers by total order value in the last 30 days",
            height=100
        )
        
        if st.button("🔄 Convert to SQL", type="primary"):
            if nl_query:
                with st.spinner("Converting to SQL..."):
                    time.sleep(1)  # Simulate processing
                    
                    # Mock SQL generation based on keywords
                    if "top" in nl_query.lower() and "customer" in nl_query.lower():
                        sql_query = """-- Generated SQL Query
SELECT 
    u.username,
    u.email,
    SUM(o.total_amount) as total_spent,
    COUNT(o.order_id) as order_count
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
    AND o.status = 'completed'
GROUP BY u.user_id, u.username, u.email
ORDER BY total_spent DESC
LIMIT 5;"""
                    else:
                        sql_query = """-- Generated SQL Query
SELECT *
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY o.order_date DESC;"""
                    
                    st.markdown("### Generated SQL Query")
                    st.code(sql_query, language="sql")
                    
                    # Optimization suggestions
                    st.markdown("### 🚀 Optimization Suggestions")
                    st.markdown("""
                    <div class="success-card">
                        <h4>✅ Query Optimizations Applied:</h4>
                        <ul>
                            <li>Added proper indexes hint for user_id and order_date</li>
                            <li>Used efficient JOIN strategy</li>
                            <li>Limited result set with TOP clause</li>
                            <li>Added appropriate WHERE clause filtering</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)

elif pages[selected_page] == "performance_analyzer":
    st.title("⚡ Query Performance Analyzer")
    st.markdown("Analyze slow queries and get AI-powered optimization recommendations.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Query Input")
        query_input = st.text_area(
            "Paste your SQL query here:",
            value="""SELECT o.order_id, u.username, p.name, oi.quantity
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-12-31'
AND p.category_id = 5
ORDER BY o.order_date DESC;""",
            height=200
        )
        
        if st.button("🔍 Analyze Performance", type="primary"):
            with st.spinner("Analyzing query performance..."):
                time.sleep(2)
                
                # Mock performance metrics
                st.markdown("### 📊 Performance Analysis Results")
                
                col_a, col_b, col_c, col_d = st.columns(4)
                with col_a:
                    st.metric("Execution Time", "2.3s", "-65%")
                with col_b:
                    st.metric("Rows Scanned", "1.2M", "+23%")
                with col_c:
                    st.metric("CPU Usage", "78%", "+12%")
                with col_d:
                    st.metric("I/O Operations", "15,234", "-45%")
                
                # Issues identified
                st.markdown("### ⚠️ Issues Identified")
                st.markdown("""
                <div class="warning-card">
                    <h4>🐌 Performance Bottlenecks:</h4>
                    <ul>
                        <li><strong>Missing Index:</strong> No index on products.category_id causing full table scan</li>
                        <li><strong>Inefficient JOIN:</strong> order_items table join could be optimized</li>
                        <li><strong>Large Date Range:</strong> Full year scan on orders table</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                # Optimization recommendations
                st.markdown("### 🚀 Optimization Recommendations")
                
                st.markdown("**1. Add Missing Indexes:**")
                st.code("""
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_orders_date_user ON orders(order_date, user_id);
                """, language="sql")
                
                st.markdown("**2. Optimized Query:**")
                st.code("""
-- Optimized version with better JOIN order and filtering
SELECT /*+ USE_INDEX(p, idx_products_category_id) */ 
       o.order_id, u.username, p.name, oi.quantity
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
JOIN users u ON o.user_id = u.user_id
WHERE p.category_id = 5
  AND o.order_date BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY o.order_date DESC;
                """, language="sql")
                
                st.markdown("**Expected Performance Improvement: 65% faster execution**")
    
    with col2:
        st.subheader("Quick Stats")
        
        # Performance trend chart
        dates = pd.date_range(start='2024-07-01', end='2024-07-26', freq='D')
        performance_data = pd.DataFrame({
            'Date': dates,
            'Avg_Response_Time': [random.uniform(1.5, 4.0) for _ in dates],
            'Query_Count': [random.randint(100, 500) for _ in dates]
        })
        
        fig = px.line(performance_data, x='Date', y='Avg_Response_Time', 
                     title="Query Performance Trend")
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Common Issues")
        issues_data = pd.DataFrame({
            'Issue': ['Missing Index', 'Poor JOIN Order', 'Large Scans', 'No WHERE Clause'],
            'Frequency': [45, 32, 28, 15]
        })
        
        fig2 = px.bar(issues_data, x='Frequency', y='Issue', orientation='h',
                     title="Most Common Query Issues")
        fig2.update_layout(height=300)
        st.plotly_chart(fig2, use_container_width=True)

elif pages[selected_page] == "index_advisor":
    st.title("📊 Automatic Index Advisor")
    st.markdown("ML-powered recommendations for optimal index strategies.")
    
    tab1, tab2, tab3 = st.tabs(["🔍 Index Analysis", "➕ Recommendations", "📈 Impact Analysis"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Current Index Analysis")
            
            # Mock current indexes
            current_indexes = pd.DataFrame({
                'Table': ['users', 'orders', 'products', 'order_items', 'users', 'orders'],
                'Index_Name': ['idx_users_email', 'idx_orders_date', 'idx_products_name', 
                              'idx_orderitems_composite', 'PRIMARY', 'idx_orders_user'],
                'Columns': ['email', 'order_date', 'name', 'order_id, product_id', 
                           'user_id', 'user_id'],
                'Type': ['BTREE', 'BTREE', 'BTREE', 'COMPOSITE', 'PRIMARY', 'BTREE'],
                'Size_MB': [12.5, 45.2, 23.1, 67.8, 8.9, 34.6],
                'Usage_Score': [85, 92, 45, 78, 100, 88],
                'Status': ['Active', 'Active', 'Underused', 'Active', 'Active', 'Active']
            })
            
            st.dataframe(current_indexes, use_container_width=True)
        
        with col2:
            st.subheader("Index Health")
            
            # Index usage distribution
            usage_data = pd.DataFrame({
                'Category': ['Highly Used (>80%)', 'Moderately Used (50-80%)', 'Underused (<50%)'],
                'Count': [4, 1, 1]
            })
            
            fig = px.pie(usage_data, values='Count', names='Category', 
                        title="Index Usage Distribution")
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
            
            st.metric("Total Index Size", "192.1 MB", "+5.2%")
            st.metric("Avg Usage Score", "81.3%", "+2.1%")
    
    with tab2:
        st.subheader("🤖 ML-Generated Index Recommendations")
        
        recommendations = pd.DataFrame({
            'Priority': ['High', 'High', 'Medium', 'Medium', 'Low'],
            'Action': ['CREATE', 'CREATE', 'DROP', 'MODIFY', 'CREATE'],
            'Table': ['products', 'orders', 'products', 'order_items', 'users'],
            'Recommendation': [
                'CREATE INDEX idx_products_category_price ON products(category_id, price)',
                'CREATE INDEX idx_orders_status_date ON orders(status, order_date)',
                'DROP INDEX idx_products_name (Low usage: 12%)',
                'MODIFY idx_orderitems_composite to include quantity',
                'CREATE INDEX idx_users_created_status ON users(created_at, status)'
            ],
            'Expected_Improvement': ['67% faster filtering', '45% faster status queries', 
                                   'Save 23.1 MB', '23% faster aggregate queries',
                                   '15% faster user analytics'],
            'Confidence': [94, 89, 98, 76, 62]
        })
        
        for _, row in recommendations.iterrows():
            priority_color = {
                'High': 'red',
                'Medium': 'orange', 
                'Low': 'green'
            }[row['Priority']]
            
            st.markdown(f"""
            <div style="border-left: 4px solid {priority_color}; padding: 1rem; margin: 1rem 0; background: #f8f9fa;">
                <h4 style="color: {priority_color};">{row['Priority']} Priority - {row['Action']}</h4>
                <p><strong>Table:</strong> {row['Table']}</p>
                <p><strong>Recommendation:</strong> {row['Recommendation']}</p>
                <p><strong>Expected Improvement:</strong> {row['Expected_Improvement']}</p>
                <p><strong>ML Confidence:</strong> {row['Confidence']}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("📋 Generate Implementation Script", type="primary"):
            st.subheader("Implementation SQL Script")
            st.code("""
-- High Priority Recommendations
CREATE INDEX idx_products_category_price ON products(category_id, price);
CREATE INDEX idx_orders_status_date ON orders(status, order_date);

-- Medium Priority Recommendations  
DROP INDEX idx_products_name;
DROP INDEX idx_orderitems_composite;
CREATE INDEX idx_orderitems_enhanced ON order_items(order_id, product_id, quantity);

-- Low Priority Recommendations (Optional)
CREATE INDEX idx_users_created_status ON users(created_at, status);

-- Monitoring queries to track impact
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes 
WHERE indexname IN ('idx_products_category_price', 'idx_orders_status_date');
            """, language="sql")
    
    with tab3:
        st.subheader("📈 Impact Analysis & Monitoring")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Before/After performance comparison
            before_after = pd.DataFrame({
                'Query_Type': ['Product Search', 'Order Status', 'User Analytics', 'Reporting'],
                'Before_ms': [2340, 1250, 890, 3400],
                'After_ms': [780, 690, 760, 2100],
                'Improvement_%': [67, 45, 15, 38]
            })
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Before', x=before_after['Query_Type'], y=before_after['Before_ms']))
            fig.add_trace(go.Bar(name='After', x=before_after['Query_Type'], y=before_after['After_ms']))
            fig.update_layout(title="Query Performance: Before vs After", barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Index size over time
            dates = pd.date_range(start='2024-07-01', end='2024-07-26', freq='D')
            size_data = pd.DataFrame({
                'Date': dates,
                'Total_Size_MB': [180 + random.uniform(-10, 15) for _ in dates],
                'Query_Performance': [100 - random.uniform(0, 30) for _ in dates]
            })
            
            fig2 = px.line(size_data, x='Date', y='Total_Size_MB', 
                          title="Index Size Growth Over Time")
            st.plotly_chart(fig2, use_container_width=True)

elif pages[selected_page] == "plan_explainer":
    st.title("📖 Query Plan Explainer")
    st.markdown("Natural language explanations of complex database execution plans.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Query Execution Plan")
        
        plan_input = st.text_area(
            "Paste your execution plan here:",
            value="""Nested Loop  (cost=1.15..8.17 rows=1 width=68)
  ->  Index Scan using idx_orders_user on orders o  (cost=0.57..4.59 rows=1 width=36)
        Index Cond: (user_id = 12345)
        Filter: ((order_date >= '2024-01-01'::date) AND (order_date <= '2024-12-31'::date))
  ->  Index Scan using idx_products_id on products p  (cost=0.58..3.60 rows=1 width=32)
        Index Cond: (product_id = order_items.product_id)
Hash Join  (cost=5.18..10.25 rows=2 width=100)
  Hash Cond: (oi.order_id = o.order_id)
  ->  Seq Scan on order_items oi  (cost=0.00..4.50 rows=150 width=32)
  ->  Hash  (cost=4.59..4.59 rows=1 width=68)""",
            height=300
        )
        
        db_engine = st.selectbox("Database Engine", ["PostgreSQL", "MySQL", "SQL Server", "Oracle"])
        
        if st.button("🔍 Explain Plan", type="primary"):
            with st.spinner("Analyzing execution plan..."):
                time.sleep(1.5)
                
                st.markdown("### 🧠 AI-Generated Explanation")
                
                explanation = """
                **Overall Strategy:** This query uses a combination of index scans and hash joins to retrieve data efficiently.
                
                **Step-by-Step Breakdown:**
                
                1. **Index Scan on Orders** (Cost: 0.57-4.59)
                   - The database starts by looking up orders for user_id 12345 using the `idx_orders_user` index
                   - This is very efficient as it directly targets the specific user
                   - Additional filtering on order_date happens after the index lookup
                
                2. **Nested Loop with Products** (Cost: 1.15-8.17)
                   - For each order found, the database looks up product details
                   - Uses `idx_products_id` index for efficient product lookups
                   - Nested loops are efficient here due to the small result set from step 1
                
                3. **Hash Join with Order Items** (Cost: 5.18-10.25)
                   - The database creates a hash table from the orders result set
                   - Performs a sequential scan on order_items (concerning for large tables)
                   - Joins order_items with the hashed orders using order_id
                
                **Performance Characteristics:**
                - **Good:** Efficient use of indexes for initial lookups
                - **Concerning:** Sequential scan on order_items table
                - **Overall Cost:** ~10.25 units (moderate for this data size)
                """
                
                st.markdown(explanation)
    
    with col2:
        if 'plan_input' in locals() and plan_input:
            st.subheader("📊 Plan Analysis")
            
            # Extract and display plan metrics
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Total Cost", "10.25", "Moderate")
                st.metric("Expected Rows", "1-2", "Small Result Set")
            with col_b:
                st.metric("Join Type", "Hash + Nested", "Mixed Strategy")
                st.metric("Index Usage", "67%", "Good")
            
            # Issues and recommendations
            st.markdown("### ⚠️ Issues Identified")
            st.markdown("""
            <div class="warning-card">
                <h4>Performance Concerns:</h4>
                <ul>
                    <li><strong>Sequential Scan:</strong> order_items table is being scanned entirely</li>
                    <li><strong>Missing Index:</strong> No index on order_items.order_id for the join</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🚀 Optimization Suggestions")
            st.markdown("""
            <div class="success-card">
                <h4>Recommended Improvements:</h4>
                <ul>
                    <li>Create index on order_items(order_id) to eliminate sequential scan</li>
                    <li>Consider composite index on orders(user_id, order_date) for better filtering</li>
                    <li>Update table statistics for better cost estimation</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Visual plan representation
            st.markdown("### 🌳 Visual Plan Tree")
            st.code("""
📊 Hash Join (cost=5.18..10.25)
├── 🔍 Seq Scan: order_items (SLOW!)
└── 📋 Hash Table
    └── 🔄 Nested Loop (cost=1.15..8.17)
        ├── 📇 Index Scan: orders.idx_orders_user ✓
        └── 📇 Index Scan: products.idx_products_id ✓
            """, language="text")

elif pages[selected_page] == "code_reviewer":
    st.title("🔍 SQL Code Reviewer")
    st.markdown("AI-powered code review for SQL scripts and stored procedures.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("SQL Code Input")
        
        code_type = st.selectbox("Code Type", ["Query", "Stored Procedure", "Function", "Trigger", "View"])
        
        sql_code = st.text_area(
            "Paste your SQL code here:",
            value="""CREATE PROCEDURE GetCustomerOrders(@CustomerId INT, @StartDate DATE = NULL)
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX)
    SET @sql = 'SELECT * FROM orders WHERE customer_id = ' + CAST(@CustomerId AS NVARCHAR(10))
    
    IF @StartDate IS NOT NULL
        SET @sql = @sql + ' AND order_date >= ''' + CAST(@StartDate AS NVARCHAR(10)) + ''''
    
    EXEC sp_executesql @sql
    
    -- Get customer details
    SELECT name, email FROM customers WHERE id = @CustomerId
END""",
            height=400
        )
        
        review_level = st.selectbox("Review Level", ["Basic", "Comprehensive", "Security Focused"])
        
        if st.button("🔍 Review Code", type="primary"):
            with st.spinner("Analyzing SQL code..."):
                time.sleep(2)
                
                st.markdown("### 📋 Code Review Results")
                
                # Severity levels
                critical_issues = []
                warnings = []
                suggestions = []
                
                if "sp_executesql" in sql_code and "CAST" in sql_code:
                    critical_issues.append({
                        "type": "SQL Injection Vulnerability",
                        "line": 4,
                        "description": "Dynamic SQL construction with string concatenation is vulnerable to SQL injection",
                        "fix": "Use parameterized queries instead"
                    })
                
                if "SELECT *" in sql_code:
                    warnings.append({
                        "type": "Performance Issue", 
                        "line": 4,
                        "description": "Using SELECT * can impact performance and maintainability",
                        "fix": "Specify exact columns needed"
                    })
                
                suggestions.append({
                    "type": "Best Practice",
                    "line": 0,
                    "description": "Add error handling and transaction management",
                    "fix": "Wrap in TRY-CATCH block"
                })
                
                # Display issues by severity
                if critical_issues:
                    st.markdown("#### 🚨 Critical Issues")
                    for issue in critical_issues:
                        st.markdown(f"""
                        <div style="border-left: 4px solid red; padding: 1rem; margin: 0.5rem 0; background: #ffe6e6;">
                            <h5 style="color: red;">🚨 {issue['type']} (Line {issue['line']})</h5>
                            <p><strong>Issue:</strong> {issue['description']}</p>
                            <p><strong>Fix:</strong> {issue['fix']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                if warnings:
                    st.markdown("#### ⚠️ Warnings") 
                    for warning in warnings:
                        st.markdown(f"""
                        <div style="border-left: 4px solid orange; padding: 1rem; margin: 0.5rem 0; background: #fff3cd;">
                            <h5 style="color: orange;">⚠️ {warning['type']} (Line {warning['line']})</h5>
                            <p><strong>Issue:</strong> {warning['description']}</p>
                            <p><strong>Fix:</strong> {warning['fix']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                if suggestions:
                    st.markdown("#### 💡 Suggestions")
                    for suggestion in suggestions:
                        st.markdown(f"""
                        <div style="border-left: 4px solid blue; padding: 1rem; margin: 0.5rem 0; background: #e7f3ff;">
                            <h5 style="color: blue;">💡 {suggestion['type']}</h5>
                            <p><strong>Suggestion:</strong> {suggestion['description']}</p>
                            <p><strong>Implementation:</strong> {suggestion['fix']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Improved version
                st.markdown("### ✨ Improved Version")
                st.code("""
CREATE PROCEDURE GetCustomerOrders(
    @CustomerId INT,
    @StartDate DATE = NULL
)
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        -- Validate input parameters
        IF @CustomerId IS NULL OR @CustomerId <= 0
        BEGIN
            RAISERROR('Invalid customer ID provided', 16, 1);
            RETURN;
        END
        
        -- Get orders with parameterized query (secure)
        SELECT 
            order_id,
            customer_id,
            order_date,
            total_amount,
            status
        FROM orders 
        WHERE customer_id = @CustomerId
            AND (@StartDate IS NULL OR order_date >= @StartDate);
        
        -- Get customer details
        SELECT 
            name,
            email,
            phone
        FROM customers 
        WHERE id = @CustomerId;
        
    END TRY
    BEGIN CATCH
        -- Error handling
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();
        
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH
END
                """, language="sql")
    
    with col2:
        st.subheader("📊 Code Quality Score")
        
        # Simulated scores
        overall_score = 65
        security_score = 30
        performance_score = 75
        maintainability_score = 80
        
        st.metric("Overall Quality", f"{overall_score}%", "-35%")
        
        scores_df = pd.DataFrame({
            'Category': ['Security', 'Performance', 'Maintainability', 'Standards'],
            'Score': [security_score, performance_score, maintainability_score, 85]
        })
        
        fig = px.bar(scores_df, x='Score', y='Category', orientation='h',
                    title="Quality Breakdown", color='Score',
                    color_continuous_scale='RdYlGn')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("🎯 Key Recommendations")
        st.markdown("""
        1. **Fix SQL Injection** - Critical security issue
        2. **Add Error Handling** - Improve robustness  
        3. **Specify Columns** - Better performance
        4. **Input Validation** - Prevent invalid data
        5. **Use Comments** - Improve documentation
        """)

elif pages[selected_page] == "regression_detector":
    st.title("📈 Performance Regression Detector")
    st.markdown("Monitor and identify when queries start performing poorly over time.")
    
    tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🔍 Query Analysis", "⚙️ Configuration"])
    
    with tab1:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Queries Monitored", "1,247", "+12")
        with col2:
            st.metric("Regressions Detected", "23", "+5") 
        with col3:
            st.metric("Avg Response Time", "890ms", "+15%")
        with col4:
            st.metric("System Health", "85%", "-3%")
        
        # Performance trend over time
        st.subheader("📈 System Performance Trends")
        
        dates = pd.date_range(start='2024-07-01', end='2024-07-26', freq='H')
        perf_data = pd.DataFrame({
            'timestamp': dates,
            'avg_response_time': [800 + random.uniform(-200, 400) + 
                                (100 if i > len(dates)*0.8 else 0) for i in range(len(dates))],
            'query_count': [random.randint(50, 200) for _ in dates],
            'error_rate': [random.uniform(0, 5) + (2 if i > len(dates)*0.8 else 0) for i in range(len(dates))]
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = px.line(perf_data, x='timestamp', y='avg_response_time',
                          title="Average Response Time Trend")
            fig1.add_hline(y=1000, line_dash="dash", line_color="red", 
                          annotation_text="Warning Threshold")
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = px.line(perf_data, x='timestamp', y='error_rate',
                          title="Error Rate Trend")
            fig2.add_hline(y=3, line_dash="dash", line_color="red",
                          annotation_text="Critical Threshold")
            st.plotly_chart(fig2, use_container_width=True)
        
        # Recent regressions
        st.subheader("🚨 Recent Performance Regressions")
        
        regressions = pd.DataFrame({
            'Query_ID': ['Q_001', 'Q_045', 'Q_123', 'Q_067', 'Q_089'],
            'Query_Type': ['User Login', 'Product Search', 'Order Report', 'Analytics', 'Inventory'],
            'Baseline_ms': [120, 450, 2100, 3400, 890],
            'Current_ms': [340, 1200, 4500, 6800, 2300],
            'Regression_%': [183, 167, 114, 100, 159],
            'Detected_At': ['2024-07-26 14:30', '2024-07-26 12:15', '2024-07-25 16:45', 
                           '2024-07-25 09:20', '2024-07-24 22:10'],
            'Status': ['🔴 Critical', '🟡 Warning', '🔴 Critical', '🔴 Critical', '🟡 Warning']
        })
        
        st.dataframe(regressions, use_container_width=True)
    
    with tab2:
        st.subheader("🔍 Individual Query Analysis")
        
        selected_query = st.selectbox("Select Query for Deep Analysis", 
                                    ["Q_001: User Login", "Q_045: Product Search", "Q_123: Order Report"])
        
        if selected_query:
            query_id = selected_query.split(":")[0]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Generate sample performance data for selected query
                query_dates = pd.date_range(start='2024-07-01', end='2024-07-26', freq='H')
                query_perf = pd.DataFrame({
                    'timestamp': query_dates,
                    'response_time': [120 + random.uniform(-30, 50) + 
                                    (200 if i > len(query_dates)*0.7 else 0) for i in range(len(query_dates))],
                    'cpu_usage': [random.uniform(10, 40) for _ in query_dates],
                    'memory_usage': [random.uniform(50, 200) for _ in query_dates]
                })
                
                fig = px.line(query_perf, x='timestamp', y='response_time',
                             title=f"Performance History: {selected_query}")
                
                # Add regression detection point
                regression_point = len(query_dates) * 0.7
                fig.add_vline(x=query_dates[int(regression_point)], 
                             line_dash="dash", line_color="red",
                             annotation_text="Regression Detected")
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Root cause analysis
                st.markdown("### 🔍 Root Cause Analysis")
                
                if query_id == "Q_001":
                    st.markdown("""
                    <div class="warning-card">
                        <h4>🔍 Analysis Results for User Login Query:</h4>
                        <ul>
                            <li><strong>Trigger Event:</strong> Database schema change on 2024-07-24</li>
                            <li><strong>Root Cause:</strong> Missing index after table restructure</li>
                            <li><strong>Impact:</strong> 183% increase in response time</li>
                            <li><strong>Affected Users:</strong> All login attempts</li>
                        </ul>
                        
                        <h4>📋 Recommended Actions:</h4>
                        <ul>
                            <li>Recreate missing index on users(email, status)</li>
                            <li>Update query statistics</li>
                            <li>Consider query plan cache refresh</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("### 📊 Query Details")
                
                query_details = {
                    "Q_001": {
                        "Query": "SELECT * FROM users WHERE email = ? AND status = 'active'",
                        "Frequency": "~500/hour",
                        "Avg_Rows": "1",
                        "Tables": "users",
                        "Indexes": "idx_users_email (MISSING)"
                    },
                    "Q_045": {
                        "Query": "SELECT p.*, c.name FROM products p JOIN categories c...",
                        "Frequency": "~200/hour", 
                        "Avg_Rows": "~25",
                        "Tables": "products, categories",
                        "Indexes": "Various (Check needed)"
                    }
                }
                
                details = query_details.get(query_id, query_details["Q_001"])
                
                for key, value in details.items():
                    st.text(f"{key}: {value}")
                
                # Performance metrics
                st.markdown("### 📈 Current Metrics")
                st.metric("Response Time", "340ms", "+183%")
                st.metric("CPU Usage", "45%", "+25%") 
                st.metric("Memory Usage", "180MB", "+12%")
                st.metric("Error Rate", "0.5%", "+0.3%")
    
    with tab3:
        st.subheader("⚙️ Monitoring Configuration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Alert Thresholds")
            
            response_threshold = st.slider("Response Time Warning (ms)", 100, 5000, 1000)
            regression_threshold = st.slider("Regression Percentage (%)", 25, 200, 50)
            error_threshold = st.slider("Error Rate Warning (%)", 1, 10, 3)
            
            st.markdown("#### Monitoring Scope")
            
            monitor_all = st.checkbox("Monitor All Queries", value=True)
            if not monitor_all:
                st.multiselect("Select Query Types", 
                              ["Login", "Search", "Reports", "Analytics", "Transactions"])
            
            monitoring_frequency = st.selectbox("Check Frequency", 
                                              ["Real-time", "Every 5 minutes", "Every 15 minutes", "Hourly"])
        
        with col2:
            st.markdown("#### Notification Settings")
            
            email_alerts = st.checkbox("Email Alerts", value=True)
            if email_alerts:
                st.text_input("Alert Email", "admin@company.com")
            
            slack_alerts = st.checkbox("Slack Integration", value=False)
            dashboard_alerts = st.checkbox("Dashboard Notifications", value=True)
            
            st.markdown("#### Historical Data")
            
            retention_period = st.selectbox("Data Retention", 
                                          ["7 days", "30 days", "90 days", "1 year"])
            
            auto_baseline = st.checkbox("Auto-update Baselines", value=True)
            baseline_window = st.selectbox("Baseline Window", 
                                         ["Last 7 days", "Last 30 days", "Last 90 days"])
        
        if st.button("💾 Save Configuration", type="primary"):
            st.success("✅ Configuration saved successfully!")
            st.info("Changes will take effect within 5 minutes.")

elif pages[selected_page] == "demo_examples":
    st.title("📚 Demo Examples & Copy-Paste Templates")
    st.markdown("Ready-to-use examples for testing each optimization tool. Simply copy and paste these into the respective sections.")
    
    # Quick navigation
    st.markdown("### 🎯 Quick Navigation")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💬 NL-to-SQL Examples"):
            st.session_state.demo_section = "nl_examples"
        if st.button("⚡ Performance Examples"):
            st.session_state.demo_section = "performance_examples"
    with col2:
        if st.button("📊 Index Examples"):
            st.session_state.demo_section = "index_examples"
        if st.button("📖 Execution Plans"):
            st.session_state.demo_section = "plan_examples"
    with col3:
        if st.button("🔍 Code Review Examples"):
            st.session_state.demo_section = "code_examples"
        if st.button("📈 Regression Scenarios"):
            st.session_state.demo_section = "regression_examples"
    
    # Initialize session state
    if 'demo_section' not in st.session_state:
        st.session_state.demo_section = "nl_examples"
    
    st.markdown("---")
    
    # Natural Language to SQL Examples
    if st.session_state.demo_section == "nl_examples":
        st.markdown("## 💬 Natural Language to SQL Examples")
        st.markdown("Copy these natural language queries and paste them in the **Natural Language to SQL** tool:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🛒 E-commerce Examples")
            
            ecommerce_examples = [
                "Show me the top 10 customers by total purchase amount this year",
                "Find all products that are out of stock in the electronics category",
                "Get the average order value for each month in 2024", 
                "List customers who haven't placed an order in the last 90 days",
                "Show me products with more than 100 units sold but less than 50 in stock",
                "Find the most popular products in each category by sales volume",
                "Get all orders placed on weekends with a value over $500",
                "Show me customers who have returned items more than 3 times",
                "Find products with the highest profit margins in each category"
            ]
            
            for i, example in enumerate(ecommerce_examples, 1):
                with st.expander(f"Example {i}: {example[:50]}..."):
                    st.code(example)
                    if st.button(f"📋 Copy", key=f"ecom_{i}"):
                        st.success("✅ Copied to clipboard! Paste in Natural Language to SQL tool.")
        
        with col2:
            st.markdown("### 👥 HR System Examples")
            
            hr_examples = [
                "Show me all employees hired in the last 6 months",
                "Find the average salary by department and years of experience", 
                "List employees whose salaries are above the department average",
                "Get the top 5 departments by employee count",
                "Show me employees working on more than 3 active projects",
                "Find employees eligible for promotion based on 5+ years experience",
                "List all managers and their direct report counts",
                "Show me the salary distribution across all departments",
                "Find employees with the most diverse skill sets"
            ]
            
            for i, example in enumerate(hr_examples, 1):
                with st.expander(f"Example {i}: {example[:50]}..."):
                    st.code(example)
                    if st.button(f"📋 Copy", key=f"hr_{i}"):
                        st.success("✅ Copied to clipboard! Paste in Natural Language to SQL tool.")
    
    # Performance Analysis Examples
    elif st.session_state.demo_section == "performance_examples":
        st.markdown("## ⚡ Query Performance Analysis Examples")
        st.markdown("Copy these slow queries and paste them in the **Query Performance Analyzer** tool:")
        
        performance_examples = {
            "Missing Index (High Impact)": """SELECT o.order_id, u.username, p.name, oi.quantity
FROM orders o
JOIN users u ON o.user_id = u.user_id  
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date BETWEEN '2024-01-01' AND '2024-12-31'
  AND p.category_id = 5
ORDER BY o.order_date DESC;""",
            
            "Poor JOIN Order": """SELECT c.customer_name, COUNT(o.order_id) as order_count,
       SUM(o.total_amount) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id  
LEFT JOIN products p ON oi.product_id = p.product_id
WHERE p.category_id IN (1, 2, 3, 4, 5)
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 5;""",
            
            "Unnecessary Subqueries": """SELECT u.username,
       (SELECT COUNT(*) FROM orders WHERE user_id = u.user_id) as order_count,
       (SELECT AVG(total_amount) FROM orders WHERE user_id = u.user_id) as avg_order,
       (SELECT MAX(order_date) FROM orders WHERE user_id = u.user_id) as last_order
FROM users u
WHERE u.created_at > '2024-01-01'
  AND (SELECT COUNT(*) FROM orders WHERE user_id = u.user_id) > 0;""",
            
            "Function in WHERE Clause": """SELECT product_id, name, price
FROM products 
WHERE UPPER(name) LIKE '%PHONE%'
  AND YEAR(created_date) = 2024
  AND price > 100
ORDER BY price DESC;""",
            
            "N+1 Query Problem": """-- This represents multiple queries being executed
SELECT user_id, username FROM users WHERE status = 'active';
-- Then for each user:
SELECT COUNT(*) FROM orders WHERE user_id = 1;
SELECT COUNT(*) FROM orders WHERE user_id = 2;
-- ... (repeats for each user)"""
        }
        
        for title, query in performance_examples.items():
            with st.expander(f"🐌 {title}"):
                st.markdown(f"**Issue:** {title}")
                st.code(query, language="sql")
                if st.button(f"📋 Copy Query", key=f"perf_{title}"):
                    st.success("✅ Copied! Paste in Query Performance Analyzer.")
                
                # Show expected improvements
                improvements = {
                    "Missing Index (High Impact)": "Expected: 65-80% faster with proper indexing",
                    "Poor JOIN Order": "Expected: 40-60% faster with optimized join sequence", 
                    "Unnecessary Subqueries": "Expected: 50-70% faster using JOINs instead",
                    "Function in WHERE Clause": "Expected: 30-50% faster avoiding functions",
                    "N+1 Query Problem": "Expected: 90%+ faster with single JOIN query"
                }
                st.info(f"💡 {improvements.get(title, 'Significant performance improvement expected')}")
    
    # Index Advisor Examples
    elif st.session_state.demo_section == "index_examples":
        st.markdown("## 📊 Index Advisor Examples")
        st.markdown("Review these scenarios in the **Index Advisor** tool:")
        
        index_scenarios = {
            "E-commerce High-Volume Scenario": {
                "description": "High-traffic e-commerce site with frequent customer lookups",
                "queries": [
                    "SELECT * FROM orders WHERE user_id = ? AND status = 'pending'",
                    "SELECT * FROM products WHERE category_id = ? AND price BETWEEN ? AND ?",
                    "SELECT * FROM users WHERE email = ?",
                    "SELECT * FROM orders WHERE order_date >= ? ORDER BY order_date DESC"
                ],
                "expected_indexes": [
                    "CREATE INDEX idx_orders_user_status ON orders(user_id, status)",
                    "CREATE INDEX idx_products_category_price ON products(category_id, price)",
                    "CREATE UNIQUE INDEX idx_users_email ON users(email)",
                    "CREATE INDEX idx_orders_date ON orders(order_date DESC)"
                ]
            },
            
            "Analytics Workload Scenario": {
                "description": "Data warehouse with complex analytical queries",
                "queries": [
                    "SELECT region, SUM(amount) FROM sales WHERE sale_date BETWEEN ? AND ? GROUP BY region",
                    "SELECT customer_type, AVG(amount) FROM sales s JOIN customers c ON s.customer_id = c.customer_id GROUP BY customer_type",
                    "SELECT * FROM sales WHERE product_category = ? AND amount > ?"
                ],
                "expected_indexes": [
                    "CREATE INDEX idx_sales_date_region ON sales(sale_date, region)",
                    "CREATE INDEX idx_sales_customer ON sales(customer_id) INCLUDE (amount)",
                    "CREATE INDEX idx_sales_category_amount ON sales(product_category, amount)"
                ]
            }
        }
        
        for scenario_name, scenario in index_scenarios.items():
            with st.expander(f"📈 {scenario_name}"):
                st.markdown(f"**Description:** {scenario['description']}")
                
                st.markdown("**Sample Queries:**")
                for i, query in enumerate(scenario['queries'], 1):
                    st.code(f"-- Query {i}\n{query}", language="sql")
                
                st.markdown("**Expected Index Recommendations:**")
                for i, index in enumerate(scenario['expected_indexes'], 1):
                    st.code(f"-- Recommendation {i}\n{index}", language="sql")
                
                if st.button(f"📋 Copy All Queries", key=f"idx_{scenario_name}"):
                    st.success("✅ Scenario copied! Use these in Index Advisor.")
    
    # Execution Plan Examples  
    elif st.session_state.demo_section == "plan_examples":
        st.markdown("## 📖 Execution Plan Examples")
        st.markdown("Copy these execution plans and paste them in the **Query Plan Explainer** tool:")
        
        plan_examples = {
            "PostgreSQL Nested Loop Plan": """Nested Loop  (cost=1.15..8.17 rows=1 width=68)
  ->  Index Scan using idx_orders_user on orders o  (cost=0.57..4.59 rows=1 width=36)
        Index Cond: (user_id = 12345)
        Filter: ((order_date >= '2024-01-01'::date) AND (order_date <= '2024-12-31'::date))
  ->  Index Scan using idx_products_id on products p  (cost=0.58..3.60 rows=1 width=32)
        Index Cond: (product_id = order_items.product_id)
Hash Join  (cost=5.18..10.25 rows=2 width=100)
  Hash Cond: (oi.order_id = o.order_id)
  ->  Seq Scan on order_items oi  (cost=0.00..4.50 rows=150 width=32)
  ->  Hash  (cost=4.59..4.59 rows=1 width=68)""",
            
            "SQL Server Plan with Issues": """SELECT Cost: 100%
  |--Compute Scalar(DEFINE:([Expr1004]=CONVERT_IMPLICIT(int,[Expr1005],0)))
       |--Stream Aggregate(GROUP BY:() DEFINE:([Expr1005]=Count(*)))
            |--Hash Match(Inner Join, HASH:([c].[customer_id])=([o].[customer_id]))
                 |--Index Seek(OBJECT:([db].[dbo].[customers].[PK_customers]), SEEK:([c].[customer_id]=[@customer_id]))
                 |--Clustered Index Scan(OBJECT:([db].[dbo].[orders].[PK_orders]), WHERE:([o].[order_date]>=[@start_date] AND [o].[order_date]<=[@end_date]))""",
            
            "MySQL EXPLAIN Output": """+----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------------+
| id | select_type | table | partitions | type  | possible_keys | key     | key_len | ref   | rows | filtered | Extra       |
+----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------------+
|  1 | SIMPLE      | c     | NULL       | const | PRIMARY       | PRIMARY | 4       | const |    1 |   100.00 | Using index |
|  1 | SIMPLE      | o     | NULL       | range | idx_date      | idx_date| 3       | NULL  | 5000 |   100.00 | Using where |
+----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------------+""",
            
            "Complex Join Plan": """Sort  (cost=858.52..861.02 rows=1000 width=68)
  Sort Key: o.order_date DESC
  ->  Hash Join  (cost=22.50..808.52 rows=1000 width=68)
        Hash Cond: (oi.product_id = p.product_id)
        ->  Hash Join  (cost=15.25..785.00 rows=1000 width=40)
              Hash Cond: (oi.order_id = o.order_id)
              ->  Seq Scan on order_items oi  (cost=0.00..735.00 rows=50000 width=12)
              ->  Hash  (cost=12.75..12.75 rows=200 width=36)
                    ->  Index Scan using idx_orders_date on orders o  (cost=0.43..12.75 rows=200 width=36)
                          Index Cond: ((order_date >= '2024-01-01'::date) AND (order_date <= '2024-12-31'::date))
        ->  Hash  (cost=4.25..4.25 rows=200 width=36)
              ->  Index Scan using idx_products_category on products p  (cost=0.43..4.25 rows=200 width=36)
                    Index Cond: (category_id = 5)"""
        }
        
        for plan_type, plan_text in plan_examples.items():
            with st.expander(f"🔍 {plan_type}"):
                st.code(plan_text, language="text")
                if st.button(f"📋 Copy Plan", key=f"plan_{plan_type}"):
                    st.success("✅ Copied! Paste in Query Plan Explainer.")
                
                # Add analysis hints
                analysis_hints = {
                    "PostgreSQL Nested Loop Plan": "Look for: Sequential scans, high cost operations, missing indexes",
                    "SQL Server Plan with Issues": "Look for: Index scans vs seeks, hash joins, sort operations", 
                    "MySQL EXPLAIN Output": "Look for: Full table scans, high row counts, missing key usage",
                    "Complex Join Plan": "Look for: Join order efficiency, proper index usage, sort operations"
                }
                st.info(f"💡 Analysis Focus: {analysis_hints.get(plan_type, 'General performance analysis')}")
    
    # Code Review Examples
    elif st.session_state.demo_section == "code_examples":
        st.markdown("## 🔍 SQL Code Review Examples")
        st.markdown("Copy these problematic code examples and paste them in the **SQL Code Reviewer** tool:")
        
        code_examples = {
            "Stored Procedure with SQL Injection": """CREATE PROCEDURE GetCustomerOrders(@CustomerId INT, @StartDate DATE = NULL)
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX)
    SET @sql = 'SELECT * FROM orders WHERE customer_id = ' + CAST(@CustomerId AS NVARCHAR(10))
    
    IF @StartDate IS NOT NULL
        SET @sql = @sql + ' AND order_date >= ''' + CAST(@StartDate AS NVARCHAR(10)) + ''''
    
    EXEC sp_executesql @sql
    
    -- Get customer details
    SELECT name, email FROM customers WHERE id = @CustomerId
END""",
            
            "Function with Performance Issues": """CREATE FUNCTION CalculateCustomerValue(@CustomerId INT)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalValue MONEY = 0
    
    -- BAD: Scalar function that will be called row-by-row
    SELECT @TotalValue = (
        SELECT SUM(total_amount) 
        FROM orders 
        WHERE customer_id = @CustomerId 
          AND status = 'completed'
          AND YEAR(order_date) = YEAR(GETDATE())  -- BAD: Function in WHERE
    )
    
    -- BAD: Additional query in function
    IF @TotalValue > 10000
        SET @TotalValue = @TotalValue * 1.1  -- 10% bonus
    
    RETURN ISNULL(@TotalValue, 0)
END""",
            
            "Problematic View Definition": """CREATE VIEW CustomerOrderSummary AS
SELECT 
    c.customer_id,
    c.customer_name,
    -- BAD: Scalar subqueries (will execute for each row)
    (SELECT COUNT(*) FROM orders WHERE customer_id = c.customer_id) as total_orders,
    (SELECT SUM(total_amount) FROM orders WHERE customer_id = c.customer_id) as total_spent,
    (SELECT MAX(order_date) FROM orders WHERE customer_id = c.customer_id) as last_order_date,
    -- BAD: Function in SELECT
    dbo.CalculateCustomerValue(c.customer_id) as customer_value
FROM customers c
WHERE c.status = 'active' """,
            
            "Trigger with Issues": """CREATE TRIGGER trg_update_inventory
ON order_items
AFTER INSERT
AS
BEGIN
    -- BAD: Cursor when set-based operation would work
    DECLARE item_cursor CURSOR FOR
        SELECT product_id, quantity FROM inserted
    
    DECLARE @ProductId INT, @Quantity INT
    OPEN item_cursor
    FETCH NEXT FROM item_cursor INTO @ProductId, @Quantity
    
    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- BAD: Individual updates instead of set-based
        UPDATE products 
        SET stock_quantity = stock_quantity - @Quantity
        WHERE product_id = @ProductId
        
        FETCH NEXT FROM item_cursor INTO @ProductId, @Quantity
    END
    
    CLOSE item_cursor
    DEALLOCATE item_cursor
END"""
        }
        
        for code_type, code_text in code_examples.items():
            with st.expander(f"🐛 {code_type}"):
                st.code(code_text, language="sql")
                if st.button(f"📋 Copy Code", key=f"code_{code_type}"):
                    st.success("✅ Copied! Paste in SQL Code Reviewer.")
                
                # Show expected issues
                issue_descriptions = {
                    "Stored Procedure with SQL Injection": "🚨 Critical: SQL injection vulnerability, no error handling",
                    "Function with Performance Issues": "⚠️ Warning: Scalar function, function in WHERE clause",
                    "Problematic View Definition": "⚠️ Warning: Multiple scalar subqueries, performance issues",
                    "Trigger with Issues": "💡 Suggestion: Use set-based operations instead of cursors"
                }
                st.warning(f"Expected Issues: {issue_descriptions.get(code_type, 'Various code quality issues')}")
    
    # Regression Scenarios
    elif st.session_state.demo_section == "regression_examples":
        st.markdown("## 📈 Performance Regression Scenarios")
        st.markdown("Use these scenarios to understand the **Regression Detector** tool:")
        
        regression_scenarios = {
            "Index Drop Regression": {
                "description": "Performance regression caused by accidentally dropping an important index",
                "timeline": [
                    "Day 1-10: Normal performance (avg 150ms)",
                    "Day 11: Index dropped during maintenance", 
                    "Day 11-15: Performance degrades (avg 2.3s, +1400%)",
                    "Day 16: Issue discovered and index recreated",
                    "Day 17+: Performance restored"
                ],
                "symptoms": [
                    "Sudden spike in query response times",
                    "Increased CPU usage on database server",
                    "User complaints about slow page loads",
                    "Query execution plans showing table scans"
                ],
                "query": "SELECT * FROM users WHERE email = 'user@example.com'"
            },
            
            "Data Growth Regression": {
                "description": "Gradual performance degradation due to table growth without proper indexing",
                "timeline": [
                    "Month 1: 100K records, 50ms avg",
                    "Month 3: 500K records, 150ms avg",
                    "Month 6: 1M records, 450ms avg", 
                    "Month 9: 2M records, 1.2s avg",
                    "Month 12: 5M records, 3.5s avg"
                ],
                "symptoms": [
                    "Gradual increase in response times",
                    "Queries that were fast becoming slower",
                    "Exponential growth in execution time",
                    "Resource utilization trending upward"
                ],
                "query": "SELECT COUNT(*) FROM orders WHERE status = 'pending'"
            },
            
            "Schema Change Regression": {
                "description": "Performance impact from database schema modifications",
                "timeline": [
                    "Week 1: Baseline performance established",
                    "Week 2: Schema change deployed (new column added)",
                    "Week 3: Gradual performance degradation noticed",
                    "Week 4: Query plans changed, using different indexes",
                    "Week 5: Statistics updated, performance improved"
                ],
                "symptoms": [
                    "Query plan changes after schema updates",
                    "Different index usage patterns",
                    "Inconsistent query performance",
                    "Need for statistics updates"
                ],
                "query": "SELECT o.*, u.username FROM orders o JOIN users u ON o.user_id = u.user_id"
            }
        }
        
        for scenario_name, scenario in regression_scenarios.items():
            with st.expander(f"📉 {scenario_name}"):
                st.markdown(f"**Description:** {scenario['description']}")
                
                st.markdown("**Timeline:**")
                for event in scenario['timeline']:
                    st.markdown(f"- {event}")
                
                st.markdown("**Symptoms to Watch For:**")
                for symptom in scenario['symptoms']:
                    st.markdown(f"- {symptom}")
                
                st.markdown("**Sample Query to Monitor:**")
                st.code(scenario['query'], language="sql")
                
                if st.button(f"📋 Copy Scenario", key=f"reg_{scenario_name}"):
                    st.success("✅ Scenario details copied! Use this context in Regression Detector.")
    
    # Getting Started Guide
    st.markdown("---")
    st.markdown("## 🚀 How to Use These Examples")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📋 Copy-Paste Instructions:
        
        1. **Click any "📋 Copy" button** above
        2. **Navigate to the appropriate tool** using the sidebar
        3. **Paste the example** into the input field
        4. **Click the analyze/process button** for that tool
        5. **Review the results** and recommendations
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Recommended Learning Path:
        
        1. **Start with NL-to-SQL examples** - See AI in action
        2. **Try Performance Analysis** - Learn optimization 
        3. **Explore Index Advisor** - Understand indexing
        4. **Review Execution Plans** - Deep technical analysis
        5. **Test Code Review** - Best practices
        6. **Setup Regression Monitoring** - Proactive monitoring
        """)
    
    # Tips and best practices
    st.markdown("### 💡 Pro Tips")
    st.markdown("""
    <div class="success-card">
        <h4>🌟 Getting the Most from These Examples:</h4>
        <ul>
            <li><strong>Compare Results:</strong> Try the same query in multiple tools to see different insights</li>
            <li><strong>Follow Recommendations:</strong> Implement the suggested optimizations and measure improvements</li>
            <li><strong>Learn Patterns:</strong> Notice common issues like missing indexes, poor JOIN orders</li>
            <li><strong>Experiment:</strong> Modify the examples to match your own database scenarios</li>
            <li><strong>Progressive Learning:</strong> Start with simple examples, then try more complex ones</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Resources")
st.sidebar.markdown("- [Documentation](https://docs.example.com)")
st.sidebar.markdown("- [API Reference](https://api.example.com)")  
st.sidebar.markdown("- [Support](mailto:support@example.com)")
st.sidebar.markdown("---")
st.sidebar.markdown("*SQL Optimizer Suite v2.1*")