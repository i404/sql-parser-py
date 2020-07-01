from parser import spark
from colorama import Fore

if __name__ == '__main__':
    show_details = True

    sql = "create table xxxx as select * from xxx.a limit 1; " \
          "select * from adad.adfas; " \
          "with c as (select * from dw.ss limit 1) select * from c; " \
          "create TEMPORARY table dwd_economy_match_tournament_detail_batch as select 1 from xx;"

    result = spark.parse_string(sql, show_details)

    print(Fore.BLUE + "input tables:" + Fore.RESET)
    for ts in result.input_tables:
        print(ts)

    print(Fore.BLUE + "output tables:" + Fore.RESET)
    for ts in result.output_tables:
        print(ts)

    if show_details:
        print("\n\n")
        print(Fore.GREEN + "details:" + Fore.RESET)
        for statement_result in result.statement_details:
            print(Fore.GREEN + "statement content:" + Fore.RESET)
            print(sql[statement_result.start:statement_result.stop])

            print(Fore.GREEN + "statement type:" + Fore.RESET)
            print(statement_result.type)

            print(Fore.GREEN + "statement input tables:" + Fore.RESET)
            for ts in statement_result.input_tables:
                print(ts)

            print(Fore.GREEN + "statement output tables:" + Fore.RESET)
            for ts in statement_result.output_tables:
                print(ts)

            print('\n\n')
