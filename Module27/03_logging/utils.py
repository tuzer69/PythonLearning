def write_log(data: str) -> None:
    with open('function_errors.log', 'a', encoding='utf-8') as log_file:
        log_file.write(data + '\n')
