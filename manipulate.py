def manipulate_data(string_type, data_to_manipulate):
  if string_type=="list":
    return data_to_manipulate[-1:: -1]        #returns the reverse of the tring type if its a list
  if string_type=="set":
    return set.union(data_to_manipulate, ["ANDELA", "TIA", "AFRICA"]) #adds items to the string type if its a set
  if string_type=="dictionary":
    return [key for key, item in data_to_manipulate.items()] #returns the keys only if its a dictionary
    
   