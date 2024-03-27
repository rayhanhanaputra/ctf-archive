
  <section class="bg-[url('/images/bg-blue.jpg')] h-screen x-screen bg-cover bg-no-repeat">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">

        <div class="min-w-[60%] w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-center text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                My Todo List
                </h1>
                <div class="flex space-x-4">
                  <div class="row">
                    <a href="#" onclick="changeTheme('red');return false;">
                      <svg class="my-2 text-red-100 hover:text-red-700 focus:text-red-700" xmlns="http://www.w3.org/2000/svg" width="30" class="mr-2" fill="currentColor" viewBox="0 0 1792 1792">
                        <path d="M1728 647q0 22-26 48l-363 354 86 500q1 7 1 20 0 21-10.5 35.5t-30.5 14.5q-19 0-40-12l-449-236-449 236q-22 12-40 12-21 0-31.5-14.5t-10.5-35.5q0-6 2-20l86-500-364-354q-25-27-25-48 0-37 56-46l502-73 225-455q19-41 49-41t49 41l225 455 502 73q56 9 56 46z">
                        </path>
                    </svg>
                    </a>
                    <a href="#" onclick="changeTheme('green');return false;">
                      <svg class="my-2 text-green-100 hover:text-green-700 focus:text-green-700" xmlns="http://www.w3.org/2000/svg" width="30" class="mr-2" fill="currentColor" viewBox="0 0 1792 1792">
                        <path d="M1728 647q0 22-26 48l-363 354 86 500q1 7 1 20 0 21-10.5 35.5t-30.5 14.5q-19 0-40-12l-449-236-449 236q-22 12-40 12-21 0-31.5-14.5t-10.5-35.5q0-6 2-20l86-500-364-354q-25-27-25-48 0-37 56-46l502-73 225-455q19-41 49-41t49 41l225 455 502 73q56 9 56 46z">
                        </path>
                      </svg>
                    </a>
                    <a href="#" onclick="changeTheme('blue');return false;">
                      <svg class="my-2 text-blue-600 hover:text-blue-700 focus:text-blue-700" xmlns="http://www.w3.org/2000/svg" width="30" class="mr-2" fill="currentColor" viewBox="0 0 1792 1792">
                        <path d="M1728 647q0 22-26 48l-363 354 86 500q1 7 1 20 0 21-10.5 35.5t-30.5 14.5q-19 0-40-12l-449-236-449 236q-22 12-40 12-21 0-31.5-14.5t-10.5-35.5q0-6 2-20l86-500-364-354q-25-27-25-48 0-37 56-46l502-73 225-455q19-41 49-41t49 41l225 455 502 73q56 9 56 46z">
                        </path>
                      </svg>
                    </a>
                    <a href="/logout.php">
                      <svg class="my-4 text-blue-600" xmlns="http://www.w3.org/2000/svg" width="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-log-out"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                    </a>
                  </div>
                  <div class="basis-1/2 w-full">
                    <div class="grid space-y-4">
                      <div class="w-full border rounded-lg p-2">
                        <p class="block text-center text-lg font-bold text-gray-900 dark:text-white">Today</p>
                        <p id="clock" class="text-center">2023-11-11 11:11:11</p>
                      </div>
                      <div class="w-full border rounded-lg p-2">
                        <p class="block text-center text-lg font-bold text-gray-900 dark:text-white">Weather</p>
                        <p class="text-center" id="weatherInfo"></p>
                      </div>
                      <div class="w-full border rounded-lg p-2">
                        <p class="block text-center text-lg font-bold text-gray-900 dark:text-white">Quote</p>
                        <p class="text-center" id="quote"></p>
                      </div>
                      
                    </div>
                  </div>
                  <div class="basis-1/2 w-full">
                    <div class="w-full border rounded-lg p-2">
                        <p class="block text-center text-lg font-bold text-gray-900 dark:text-white">Todos</p>
                        <div class="p-2">
                          
                          <div id="addList" class="max-h-64 overflow-auto">
                          <?php foreach ($todos_row as $todo): ?>
                            <div class="Todo relative flex items-center border rounded p-2 mb-4">
                                <label for="default-checkbox" class="cursor-pointer text-sm font-medium text-gray-900 dark:text-gray-300">
                                  <input type="checkbox" onchange="todoDone('<?php echo $todo['id']; ?>')" value="" <?php if ($todo['done'] == 1): ?>checked="true"<?php endif; ?> class="cursor-pointer align-[-3px] w-4 h-4 mr-2 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                <span><?php echo $todo["task"]; ?></span></label>
                                <button type="button" onclick="removeTodo(this, <?php echo $todo['id']; ?>)" class="absolute right-2 bg-white rounded-md inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
                                  <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                  </svg>
                                </button>
                            </div>
                          <?php endforeach; ?>  
                          </div>
                          <button type="button" onclick="showTodo()" class="mt-4 w-full text-white bg-blue-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Add</button>
                        </div>
                        
                      </div>
                  </div>
                </div>
            </div>
        </div>
    </div>
  </section>

  <!-- modal -->
  <div id="addModal" class="relative z-10 hidden" aria-labelledby="modal-title" role="dialog" aria-modal="true">
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>
    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
        <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <form id="addForm">
            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
              <div class="w-full">
                <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                  <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Add</h3>
                  <div class="mt-2">
                      <div id="addTodoList" class="justify-between items-center rounded py-2">
                          <div class="w-full my-2">
                            <input type="text" name="addText" id="addText" value="" class="p-1.5 w-full border text-sm font-medium text-gray-900 dark:text-gray-300 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" placeholder="Write todo ...">
                          </div>
                      </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="bg-gray-50 px-4 py-3 justify-center texgt-center sm:flex sm:flex-row-reverse sm:px-6">
              <button type="button" onclick="addTodo()" class="inline-flex w-full justify-center rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-500 sm:ml-3 sm:w-auto">Add</button>
              <button type="button" onclick="closeTodo()" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cancel</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <!-- new Todo -->
  <div id="newTodo" class="Todo hidden relative flex items-center border rounded p-2 mb-4">
      <label for="default-checkbox" class="cursor-pointer text-sm font-medium text-gray-900 dark:text-gray-300">
        <input type="checkbox" value="" class="cursor-pointer align-[-3px] w-4 h-4 mr-2 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
      <span>Todo 1</span></label>
      <button type="button" onclick="removeTodo(this, false)" class="absolute right-2 bg-white rounded-md inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
  </div>
