class ExpanseTracker:
    def __init__(self):
        self.expanses = []
        self.id_counter = 1
    
    def add_expance(self, description, amount):
        expanse = {
            "id": self.id_counter,
            "description": description,
            "amount": amount
        }
        
        self.expanses.append(expanse)
        self.id_counter += 1
        print(f"Qo'shildi: {description} - ${amount}")
        
    def view_expanse(self):
        if not self.expanses:
            print("Xarajatlar yoq")
        else:
            print("\nXarajatlar royxati")
            for expanse in self.expanses:
                print(f"{expanse["id"]}. {expanse["description"]} - ${expanse["amount"]}")
                
    def delete_expanse(self,expanse_id):
        for expanse in self.expanses:
            if expanse["id"] == expanse_id:
                self.expanses.remove(expanse) 
                print(f"{expanse_id} ID raqamli xarajat ochirildi.") 
                return
        print(f"{expanse_id} ID rarqamli xarajat topilmadi.")
        
    def main(self):
        while True:
            print("\n -- Xarajatlarni boshqarish --")
            print("1. Xarajat qo'shish.")
            print("2. Xarajat ko'rish.")
            print("3. Xarjat ochirish.")
            print("4. Chiqish.")
            choise = input("\nTanlang: ")
            if choise =="1":
                description = input("Xarajatni kiriting: ")
                amount = float(input("Summani kiriting: "))
                self.add_expance(description, amount)  
            elif choise == "2":
                self.view_expanse ()    
            elif choise == "3":
                expanse_id = int(input("Ochirilgan xarajat ID raqamini kiriting"))
                self.delete_expanse(expanse_id)
            elif choise == "4":
                print("Chiqdingiz.")  
                break
            else:
                print("Notog'ri buyruq, qayta urinib kuring.")
            
tracker = ExpanseTracker() 
tracker.main()    
 