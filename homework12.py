import asyncio, time

async def execute_files(file_number):
    global total_result
    with open (f'./data/in_{file_number}.dat') as datafile:
        operation_code = datafile.readline().rstrip()
        number1, number2 = map(float, datafile.readline().split())
        if operation_code == '1':
            result = number1 + number2
        elif operation_code == '2':
            result = number1 * number2
        elif operation_code == '3':
            result = number1 * number1 + number2 * number2
        with open ('./log_file.dat', 'a') as log_file:
            log_file.write(f'File #{file_number} Result: {result}\n')#
            total_result += result
     

if __name__ == '__main__':
    start_time = time.time()
    total_result = 0.0
    event_loop = asyncio.get_event_loop()
    tasks = [event_loop.create_task(execute_files(_)) for _ in range(10000)]
    wait_tasks = asyncio.wait(tasks)
    event_loop.run_until_complete(wait_tasks)
    event_loop.close()
    with open ('./out.dat', 'w') as result_file:
        result_file.write(str(total_result))
    total_time = time.time() - start_time
    print(f'10000 files prepared at {total_time}')
    

