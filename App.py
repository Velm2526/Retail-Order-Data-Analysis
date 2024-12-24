import streamlit as st
import mysql.connector
import pandas as pd

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",  # Your MySQL host
        user="root",        # Your MySQL username
        password="2526",    # Your MySQL password
        database="Retail_order"  # Your database name
    )
    return connection

# Function to execute the SQL query and return a DataFrame
def run_query(query):
    connection = get_db_connection()
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Streamlit app layout
def main():
    st.title('Retail Orders Analytics')

    # Sidebar for selecting which analysis to perform
    analysis_choice = st.sidebar.selectbox(
        "Choose an Analysis",
        [
            "Top 10 Highest Revenue Generating Products",
            "Top 5 Cities with Highest Profit Margins",
            "Total Discount Given per Category",
            "Average Sale Price per Product Category",
            "Region with Highest Average Sale Price",
            "Total Profit per Category",
            "Top 3 Segments with Highest Quantity of Orders",
            "Average Discount Percentage per Region",
            "Product Category with Highest Total Profit",
            "Total Revenue Generated per Year",
            "Create a query where the order id has same value",
            "INNER JOIN based on product_id", 
            "RIGHT JOIN based on order_id",   
            "RIGHT JOIN based on product_id",  
            "Get Orders and Profits by Region and Ship Mode",
            "Calculate Total Sales and Profit by Category and Subcategory",
            "Calculate Total Sales and Profit for Each Product",
            "Get the Most Expensive Order for Each Category"
        ]
    )

    # Perform analysis based on user selection
    if analysis_choice == "Top 10 Highest Revenue Generating Products":
        query = """
        SELECT product_id,
               SUM(sale_price * quantity) AS total_revenue
        FROM retailorders
        GROUP BY product_id
        ORDER BY total_revenue DESC
        LIMIT 10;
        """
        df = run_query(query)
        st.write("Top 10 Highest Revenue Generating Products")
        st.dataframe(df)

    elif analysis_choice == "Get Orders and Profits by Region and Ship Mode":
        query = """
        SELECT 
            region,
            ship_mode,
            SUM(profit) AS total_profit
        FROM 
            retailorders
        GROUP BY 
            region, ship_mode
        ORDER BY 
            total_profit DESC;
        """
        df = run_query(query)
        st.write("Get Orders and Profits by Region and Ship Mode")
        st.dataframe(df)

    elif analysis_choice == "Calculate Total Sales and Profit for Each Product":
        query = """
        SELECT 
            product_id,
            SUM(sale_price) AS total_sales,
            SUM(profit) AS total_profit
        FROM 
            retailorders
        GROUP BY 
            product_id
        ORDER BY 
            total_sales DESC;
        """
        df = run_query(query)
        st.write("Calculate Total Sales and Profit for Each Product")
        st.dataframe(df)

    elif analysis_choice == "Calculate Total Sales and Profit by Category and Subcategory":
        query = """
        SELECT 
            category,
            sub_category,
            SUM(sale_price) AS total_sales,
            SUM(profit) AS total_profit
        FROM 
            retailorders
        GROUP BY 
            category, sub_category
        ORDER BY 
            total_sales DESC;
        """
        df = run_query(query)
        st.write("Calculate Total Sales and Profit by Category and Subcategory")
        st.dataframe(df)

    elif analysis_choice == "Create a query where the order id has same value":
        query = """
        SELECT 
            rs.order_id,
            rs.order_date,
            rs.ship_mode,
            rs.segment,
            rs.country,
            rs.city,
            rs.state,
            rs.postal_code,
            rs.region,
            rs.category AS order_category,
            rs.sub_category AS order_sub_category,
            rs.product_id,
            rs.cost_price AS order_cost_price,
            rs.list_price AS order_list_price,
            rs.quantity AS order_quantity,
            rs.discount_percent AS order_discount_percent,
            rs.discount AS order_discount,
            rs.sale_price AS order_sale_price,
            rs.profit AS order_profit,
            ps.category AS product_category,
            ps.sub_category AS product_sub_category,
            ps.cost_price AS product_cost_price,
            ps.list_price AS product_list_price,
            ps.quantity AS product_quantity,
            ps.discount_percent AS product_discount_percent,
            ps.discount AS product_discount,
            ps.sale_price AS product_sale_price,
            ps.profit AS product_profit
        FROM 
            retailorders AS rs
        INNER JOIN 
            productdetretailordersails AS ps
            ON rs.order_id = ps.order_id;
        """
        df = run_query(query)
        st.write("Create a query where the order id has the same value")
        st.dataframe(df)

    elif analysis_choice == "Get the Most Expensive Order for Each Category":
        query = """
        SELECT 
            category,
            MAX(sale_price) AS most_expensive_order
        FROM 
            retailorders
        GROUP BY 
            category;
        """
        df = run_query(query)
        st.write("Get the Most Expensive Order for Each Category")
        st.dataframe(df)

    elif analysis_choice == "INNER JOIN based on product_id":
        query = """
        SELECT 
            ro.order_id,
            ro.order_date,
            ro.ship_mode,
            ro.segment,
            ro.country,
            ro.city,
            ro.state,
            ro.postal_code,
            ro.region,
            ro.category AS order_category,
            ro.sub_category AS order_sub_category,
            ro.product_id,
            ro.cost_price AS order_cost_price,
            ro.list_price AS order_list_price,
            ro.quantity AS order_quantity,
            ro.discount_percent AS order_discount_percent,
            ro.discount AS order_discount,
            ro.sale_price AS order_sale_price,
            ro.profit AS order_profit,
            pds.category AS product_category,
            pds.sub_category AS product_sub_category,
            pds.cost_price AS product_cost_price,
            pds.list_price AS product_list_price,
            pds.quantity AS product_quantity,
            pds.discount_percent AS product_discount_percent,
            pds.discount AS product_discount,
            pds.sale_price AS product_sale_price,
            pds.profit AS product_profit
        FROM 
            retailorders ro
        INNER JOIN 
            productdetretailordersails pds
            ON ro.product_id = pds.product_id;
        """
        df = run_query(query)
        st.write("INNER JOIN based on product_id")
        st.dataframe(df)

    elif analysis_choice == "RIGHT JOIN based on order_id":
        query = """
        SELECT 
            ro.order_id,
            ro.order_date,
            ro.ship_mode,
            ro.segment,
            ro.country,
            ro.city,
            ro.state,
            ro.postal_code,
            ro.region,
            ro.category AS order_category,
            ro.sub_category AS order_sub_category,
            ro.product_id,
            ro.cost_price AS order_cost_price,
            ro.list_price AS order_list_price,
            ro.quantity AS order_quantity,
            ro.discount_percent AS order_discount_percent,
            ro.discount AS order_discount,
            ro.sale_price AS order_sale_price,
            ro.profit AS order_profit,
            pds.category AS product_category,
            pds.sub_category AS product_sub_category,
            pds.cost_price AS product_cost_price,
            pds.list_price AS product_list_price,
            pds.quantity AS product_quantity,
            pds.discount_percent AS product_discount_percent,
            pds.discount AS product_discount,
            pds.sale_price AS product_sale_price,
            pds.profit AS product_profit
        FROM 
            retailorders ro
        RIGHT JOIN 
            productdetretailordersails pds
            ON ro.order_id = pds.order_id;
        """
        df = run_query(query)
        st.write("RIGHT JOIN based on order_id")
        st.dataframe(df)

    elif analysis_choice == "RIGHT JOIN based on product_id":
        query = """
        SELECT 
            ro.order_id,
            ro.order_date,
            ro.ship_mode,
            ro.segment,
            ro.country,
            ro.city,
            ro.state,
            ro.postal_code,
            ro.region,
            ro.category AS order_category,
            ro.sub_category AS order_sub_category,
            ro.product_id,
            ro.cost_price AS order_cost_price,
            ro.list_price AS order_list_price,
            ro.quantity AS order_quantity,
            ro.discount_percent AS order_discount_percent,
            ro.discount AS order_discount,
            ro.sale_price AS order_sale_price,
            ro.profit AS order_profit,
            pds.category AS product_category,
            pds.sub_category AS product_sub_category,
            pds.cost_price AS product_cost_price,
            pds.list_price AS product_list_price,
            pds.quantity AS product_quantity,
            pds.discount_percent AS product_discount_percent,
            pds.discount AS product_discount,
            pds.sale_price AS product_sale_price,
            pds.profit AS product_profit
        FROM 
            retailorders ro
        RIGHT JOIN 
            productdetretailordersails pds
            ON ro.product_id = pds.product_id;
        """
        df = run_query(query)
        st.write("RIGHT JOIN based on product_id")
        st.dataframe(df)

if __name__ == "__main__":
    main()
