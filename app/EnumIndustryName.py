from enum import Enum
class IndustryName(Enum):
   OIL_GAS = "Oil and Gas"
   INFORMATION_TECHNOLOGY = "Information Technology"
   AUTOMOTIVES="Automotives"
   RealState="Realestate"
   Construction="Construction"
   Electricity="Electricity"
   Tourism="Tourism"
   Steel="Steel"
   Food_bvrg_retail="Food and beverage (retail)"
   Sugar="Sugar"
   Grains="Grains"
   Cotton="Cotton"
   Fruits_and_vegetables="Fruits and vegetables"
   Fertilizers="Fertilizers"
   Oil_Refining_Extraction="Food & Beverage (Oil Refining & Extraction)"
   Meat = "Food & Beverage (Meat)"
   Dairy_Cheese= "Food & Beverage (Dairy & Cheese)"
   Textiles="Textiles"


   @classmethod
   def get_key(cls, value:str)->str:
      """Retrieve the key for a given value."""
      for item in cls:
         if item.value == value:
               return item.name
      return None

   @classmethod
   def get_value(cls, key:str) -> str:
      """Retrieve the value for a given key."""
      if key in cls.__members__:
         return cls[key].value
      return None
   
   @classmethod
   def get_value(cls, key:str) -> str:
      """Retrieve the value for a given key."""
      if key in cls.__members__:
         return cls[key].value
      return None
   
   @classmethod
   def get_all_keys(cls)->list[str]:
      """Return a list of all keys in the enum."""
      return [item.name for item in cls]

   @classmethod
   def get_all_values(cls)->list[str]:
      """Return a list of all values in the enum."""
      return [item.value for item in cls]
   