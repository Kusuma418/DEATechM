from welcome import show_welcome
from services.insert_service import insert_all_stocks
from stock_analysis import StockAnalyzer

def main():
    while True:
        show_welcome()
        choice = input("Enter your choice (1-12): ").strip()

        if choice == '1':
            insert_all_stocks()
        elif choice in [str(i) for i in range(2, 12)]:
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper().strip()
            analyzer = StockAnalyzer(symbol)

            if choice == '2':
                analyzer.compare_volume_vs_price()
            elif choice == '3':
                analyzer.analyze_volatility()
            elif choice == '4':
                analyzer.historical_trend()
            elif choice == '5':
                analyzer.analyze_drawdown()
            elif choice == '6':
                analyzer.absolute_return()
            elif choice == '7':
                analyzer.cagr()
            elif choice == '8':
                analyzer.days_above_previous_close()
            elif choice == '9':
                analyzer.moving_averages()
            elif choice == '10':
                analyzer.generate_signal()
            elif choice == '11':
                analyzer.final_score()

        elif choice == '12':
            print("Exiting. Thank you for using RevStox!")
            break
        else:
            print("Invalid choice. Please enter a valid number (1-12).")

if __name__ == "__main__":
    main()