"""
Number System Converter & Calculator
Binary, Decimal, Octal, Hexadecimal conversions with arithmetic operations
"""

class NumberSystemConverter:
    """Complete Number System Converter with multiple functionalities"""
    
    def __init__(self):
        self.history = []
    
    # ============ CONVERSION FUNCTIONS ============
    
    def binary_to_decimal(self, binary):
        """Convert binary to decimal with step-by-step explanation"""
        try:
            binary = str(binary).strip()
            if not all(bit in '01' for bit in binary):
                raise ValueError("Invalid binary number")
            
            decimal = 0
            print(f"\nConverting Binary {binary} to Decimal:")
            print("-" * 50)
            
            for i, bit in enumerate(reversed(binary)):
                power = i
                value = int(bit) * (2 ** power)
                decimal += value
                print(f"Position {i}: {bit} × 2^{power} = {value}")
            
            print(f"\nResult: {binary} (Binary) = {decimal} (Decimal)")
            self.history.append(f"{binary}₂ = {decimal}₁₀")
            return decimal
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def decimal_to_binary(self, decimal):
        """Convert decimal to binary with step-by-step explanation"""
        try:
            decimal = int(decimal)
            if decimal < 0:
                raise ValueError("Negative numbers not supported")
            
            print(f"\nConverting Decimal {decimal} to Binary:")
            print("-" * 50)
            
            if decimal == 0:
                return "0"
            
            binary = ""
            temp = decimal
            steps = []
            
            while temp > 0:
                remainder = temp % 2
                quotient = temp // 2
                steps.append(f"{temp} ÷ 2 = {quotient}, Remainder = {remainder}")
                binary = str(remainder) + binary
                temp = quotient
            
            for step in steps:
                print(step)
            
            print(f"\nReading remainders from bottom to top:")
            print(f"Result: {decimal} (Decimal) = {binary} (Binary)")
            self.history.append(f"{decimal}₁₀ = {binary}₂")
            return binary
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def decimal_to_octal(self, decimal):
        """Convert decimal to octal"""
        try:
            decimal = int(decimal)
            octal = oct(decimal)[2:]
            print(f"{decimal} (Decimal) = {octal} (Octal)")
            self.history.append(f"{decimal}₁₀ = {octal}₈")
            return octal
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def decimal_to_hexadecimal(self, decimal):
        """Convert decimal to hexadecimal"""
        try:
            decimal = int(decimal)
            hexadecimal = hex(decimal)[2:].upper()
            print(f"{decimal} (Decimal) = {hexadecimal} (Hexadecimal)")
            self.history.append(f"{decimal}₁₀ = {hexadecimal}₁₆")
            return hexadecimal
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def binary_to_octal(self, binary):
        """Convert binary to octal"""
        decimal = self.binary_to_decimal(binary)
        if decimal is not None:
            return self.decimal_to_octal(decimal)
        return None
    
    def binary_to_hexadecimal(self, binary):
        """Convert binary to hexadecimal"""
        decimal = self.binary_to_decimal(binary)
        if decimal is not None:
            return self.decimal_to_hexadecimal(decimal)
        return None
    
    # ============ ARITHMETIC OPERATIONS ============
    
    def binary_addition(self, bin1, bin2):
        """Add two binary numbers"""
        try:
            dec1 = int(bin1, 2)
            dec2 = int(bin2, 2)
            result = dec1 + dec2
            binary_result = bin(result)[2:]
            
            print(f"\nBinary Addition:")
            print(f"  {bin1}")
            print(f"+ {bin2}")
            print(f"= {binary_result}")
            print(f"\nIn Decimal: {dec1} + {dec2} = {result}")
            
            return binary_result
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def binary_subtraction(self, bin1, bin2):
        """Subtract two binary numbers"""
        try:
            dec1 = int(bin1, 2)
            dec2 = int(bin2, 2)
            result = dec1 - dec2
            binary_result = bin(result)[2:] if result >= 0 else f"-{bin(abs(result))[2:]}"
            
            print(f"\nBinary Subtraction:")
            print(f"  {bin1}")
            print(f"- {bin2}")
            print(f"= {binary_result}")
            print(f"\nIn Decimal: {dec1} - {dec2} = {result}")
            
            return binary_result
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def binary_multiplication(self, bin1, bin2):
        """Multiply two binary numbers"""
        try:
            dec1 = int(bin1, 2)
            dec2 = int(bin2, 2)
            result = dec1 * dec2
            binary_result = bin(result)[2:]
            
            print(f"\nBinary Multiplication:")
            print(f"  {bin1} × {bin2} = {binary_result}")
            print(f"\nIn Decimal: {dec1} × {dec2} = {result}")
            
            return binary_result
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    # ============ UTILITY FUNCTIONS ============
    
    def complement_1s(self, binary):
        """Find 1's complement of binary number"""
        complement = ''.join('1' if bit == '0' else '0' for bit in binary)
        print(f"1's Complement of {binary} = {complement}")
        return complement
    
    def complement_2s(self, binary):
        """Find 2's complement of binary number"""
        ones_comp = self.complement_1s(binary)
        decimal = int(ones_comp, 2) + 1
        twos_comp = bin(decimal)[2:]
        print(f"2's Complement of {binary} = {twos_comp}")
        return twos_comp
    
    def show_all_representations(self, number, base=10):
        """Show number in all systems"""
        try:
            if base == 2:
                decimal = int(number, 2)
            elif base == 8:
                decimal = int(number, 8)
            elif base == 16:
                decimal = int(number, 16)
            else:
                decimal = int(number)
            
            print(f"\n{'='*50}")
            print(f"All Representations of: {number} (Base {base})")
            print(f"{'='*50}")
            print(f"Decimal      : {decimal}")
            print(f"Binary       : {bin(decimal)[2:]}")
            print(f"Octal        : {oct(decimal)[2:]}")
            print(f"Hexadecimal  : {hex(decimal)[2:].upper()}")
            print(f"{'='*50}")
            
        except Exception as e:
            print(f"Error: {e}")
    
    def show_history(self):
        """Display conversion history"""
        if not self.history:
            print("\nNo conversion history yet!")
            return
        
        print("\n" + "="*50)
        print("CONVERSION HISTORY")
        print("="*50)
        for i, item in enumerate(self.history, 1):
            print(f"{i}. {item}")
        print("="*50)


# ============ MAIN MENU SYSTEM ============

def main_menu():
    """Interactive menu system"""
    converter = NumberSystemConverter()
    
    while True:
        print("\n" + "="*60)
        print("        NUMBER SYSTEM CONVERTER & CALCULATOR")
        print("="*60)
        print("\n[1] Binary ↔ Decimal Conversion")
        print("[2] All Number System Conversions")
        print("[3] Binary Arithmetic Operations")
        print("[4] 1's & 2's Complement")
        print("[5] Show All Representations")
        print("[6] Conversion History")
        print("[0] Exit")
        print("-"*60)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            print("\n1. Binary to Decimal")
            print("2. Decimal to Binary")
            sub_choice = input("Choose: ").strip()
            
            if sub_choice == "1":
                binary = input("Enter binary number: ").strip()
                converter.binary_to_decimal(binary)
            elif sub_choice == "2":
                decimal = input("Enter decimal number: ").strip()
                converter.decimal_to_binary(decimal)
        
        elif choice == "2":
            print("\n1. Decimal to Octal")
            print("2. Decimal to Hexadecimal")
            print("3. Binary to Octal")
            print("4. Binary to Hexadecimal")
            sub_choice = input("Choose: ").strip()
            
            if sub_choice == "1":
                decimal = input("Enter decimal number: ").strip()
                converter.decimal_to_octal(decimal)
            elif sub_choice == "2":
                decimal = input("Enter decimal number: ").strip()
                converter.decimal_to_hexadecimal(decimal)
            elif sub_choice == "3":
                binary = input("Enter binary number: ").strip()
                converter.binary_to_octal(binary)
            elif sub_choice == "4":
                binary = input("Enter binary number: ").strip()
                converter.binary_to_hexadecimal(binary)
        
        elif choice == "3":
            print("\n1. Binary Addition")
            print("2. Binary Subtraction")
            print("3. Binary Multiplication")
            sub_choice = input("Choose: ").strip()
            
            bin1 = input("Enter first binary number: ").strip()
            bin2 = input("Enter second binary number: ").strip()
            
            if sub_choice == "1":
                converter.binary_addition(bin1, bin2)
            elif sub_choice == "2":
                converter.binary_subtraction(bin1, bin2)
            elif sub_choice == "3":
                converter.binary_multiplication(bin1, bin2)
        
        elif choice == "4":
            binary = input("Enter binary number: ").strip()
            print("\n1. 1's Complement")
            print("2. 2's Complement")
            sub_choice = input("Choose: ").strip()
            
            if sub_choice == "1":
                converter.complement_1s(binary)
            elif sub_choice == "2":
                converter.complement_2s(binary)
        
        elif choice == "5":
            number = input("Enter number: ").strip()
            print("\n1. Decimal")
            print("2. Binary")
            print("3. Octal")
            print("4. Hexadecimal")
            base_choice = input("Enter current base: ").strip()
            
            base_map = {"1": 10, "2": 2, "3": 8, "4": 16}
            base = base_map.get(base_choice, 10)
            converter.show_all_representations(number, base)
        
        elif choice == "6":
            converter.show_history()
        
        elif choice == "0":
            print("\nThank you for using Number System Converter!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")


# ============ RUN THE PROGRAM ============

if __name__ == "__main__":
    # Quick Demo
    print("🔢 QUICK DEMO 🔢")
    demo = NumberSystemConverter()
    
    print("\n1️⃣ Binary to Decimal:")
    demo.binary_to_decimal("1101")
    
    print("\n2️⃣ Decimal to Binary:")
    demo.decimal_to_binary(25)
    
    print("\n3️⃣ Binary Addition:")
    demo.binary_addition("1010", "1100")
    
    print("\n4️⃣ All Representations:")
    demo.show_all_representations(42)
    
    print("\n" + "="*60)
    input("\nPress Enter to start interactive menu...")
    
    # Start Interactive Menu
    main_menu()