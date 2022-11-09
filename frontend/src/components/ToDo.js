import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.add_datetime}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.is_active}
            </td>
        </tr>
)
}
const ToDoList = ({todos}) => {
    return (
    <table>
        <th>
            project
        </th>
        <th>
            text
        </th>
        <th>
            add_datetime
        </th>
        <th>
            user
        </th>
        <th>
            is_active
        </th>
        {todos.map((todo) => <ToDoItem todo={todo} />)}
    </table>
)
}
export default ToDoList