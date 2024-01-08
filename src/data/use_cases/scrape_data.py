import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd

class Scrape_data:
    def __init__(self) -> None:
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['isac']
        self.collection = self.db['flow_datas']
        
    
    def execute(self, flow_data_id: str) -> None:
        query = {"_id": ObjectId(flow_data_id)}
        document = self.collection.find_one(query)

        if document is None:
            raise Exception('Flow data not found')
        
        if 'data' in document and 'sales_history' in document['data']:
            sales_history = document['data']['sales_history']
            color_std = self.__calculate_color_std(sales_history)
            average_days_between_purchases = self.__calculate_average_days_between_purchases(sales_history)
            std_deviation_of_purchase_intervals = self.__calculate_std_deviation_of_purchase_intervals(sales_history)
            average_purchase_value = self.__calculate_average_purchase_value(sales_history)
            average_items_per_purchase = self.__calculate_average_items_per_purchase(sales_history)
            mode_of_purchased_colors = self.__calculate_mode_of_purchased_colors(sales_history)
            mode_of_purchase_weeks = self.__calculate_mode_of_purchase_weeks(sales_history)
            mode_of_payment_methods = self.__calculate_mode_of_payment_methods(sales_history)

            data = {
                "color_std": color_std,
                "average_days_between_purchases": average_days_between_purchases,
                "std_deviation_of_purchase_intervals": std_deviation_of_purchase_intervals,
                "average_purchase_value": average_purchase_value,
                "average_items_per_purchase": average_items_per_purchase,
                "mode_of_purchased_colors": mode_of_purchased_colors,
                "mode_of_purchase_weeks": mode_of_purchase_weeks,
                "mode_of_payment_methods": mode_of_payment_methods
            }

            return data

    @classmethod
    def __calculate_mode_of_purchased_colors(cls, sales_history: list) -> list:
        """
            Calculate the mode of the colors purchased
        """
        sales_history = pd.DataFrame(sales_history)
        sales_history['color'] = sales_history['items'].apply(lambda x: x[0]['name'].split("|")[-1].strip())
        sales_history = sales_history[['color', 'quantity']]
        sales_history = sales_history.groupby('color').sum()
        sales_history = sales_history.reset_index()
        sales_history = sales_history.sort_values('quantity', ascending=False)
        sales_history = sales_history.head(3)
        sales_history = sales_history['color'].tolist()
        return sales_history

    @classmethod
    def __calculate_color_std(cls, sales_history: list) -> float:
        """
            Calculate the standard deviation of the quantity of items sold per color
        """
        df_sales_history = pd.DataFrame(sales_history)
        df_sales_history['color'] = df_sales_history['items'].apply(lambda x: x[0]['name'].split("|")[-1].strip())
        df_sales_history = df_sales_history[['color', 'quantity']]
        df_sales_history = df_sales_history.groupby('color').sum()
        df_sales_history = df_sales_history.reset_index()
        df_sales_history = df_sales_history.sort_values('quantity', ascending=False)
        df_sales_history = df_sales_history['quantity'].std()
        return df_sales_history
    
    @classmethod
    def __calculate_average_items_per_purchase(cls, sales_history: list) -> float:
        """
            Calculate the average items per purchase
        """
        sales_history = pd.DataFrame(sales_history)
        sales_history['items'] = sales_history['items'].apply(lambda x: len(x))
        sales_history = sales_history['items'].mean()
        return sales_history
       
    
    @classmethod
    def __calculate_average_days_between_purchases(cls, sales_history: list) -> float:
        """
            Calculate the average days between purchases
        """
        sales_history = pd.DataFrame(sales_history)
        sales_history['createdAt'] = pd.to_datetime(sales_history['createdAt'])
        sales_history = sales_history.sort_values('createdAt', ascending=False)
        sales_history = sales_history['createdAt'].diff().mean()
        return sales_history
    
    @classmethod
    def __calculate_std_deviation_of_purchase_intervals(cls, sales_history: list) -> float:
        """
            Calculate the standard deviation of the purchase intervals
        """
        sales_history = pd.DataFrame(sales_history)
        sales_history['createdAt'] = pd.to_datetime(sales_history['createdAt'])
        sales_history = sales_history.sort_values('createdAt', ascending=False)
        sales_history = sales_history['createdAt'].diff().std()
        return sales_history
    
    @classmethod
    def __calculate_average_purchase_value(cls, sales_history: list) -> float:
        """
            Calculate the average purchase value
        """
        sales_history = pd.DataFrame(sales_history)
        sales_history['total'] = sales_history['items'].apply(lambda x: x[0]['price'])
        sales_history = sales_history['total'].mean()
        return sales_history
    
    @classmethod
    def __calculate_mode_of_purchase_weeks(cls, sales_history: list) -> list:
        """
            Calculate the mode of the weeks of the purchases
        """
        sales_history = pd.DataFrame(sales_history)
        sales_history['createdAt'] = pd.to_datetime(sales_history['createdAt'])
        sales_history['week'] = sales_history['createdAt'].dt.week
        sales_history = sales_history[['week', 'quantity']]
        sales_history = sales_history.groupby('week').sum()
        sales_history = sales_history.reset_index()
        sales_history = sales_history.sort_values('quantity', ascending=False)
        sales_history = sales_history.head(3)
        sales_history = sales_history['week'].tolist()
        return sales_history

    @classmethod
    def __calculate_mode_of_payment_methods(cls, sales_history: list) -> list:
        """
            Calculate the mode of the payment methods
        """ 
        sales_history = pd.DataFrame(sales_history)
        sales_history['payment_method'] = sales_history['payment'].apply(lambda x: x['method'])
        sales_history = sales_history[['payment_method', 'quantity']]
        sales_history = sales_history.groupby('payment_method').sum()
        sales_history = sales_history.reset_index()
        sales_history = sales_history.sort_values('quantity', ascending=False)
        sales_history = sales_history.head(3)
        sales_history = sales_history['payment_method'].tolist()
        return sales_history
        

