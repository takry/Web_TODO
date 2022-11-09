import React from 'react'

const ProjectItem = ({project, delete_project}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.url_repo}
            </td>
            <td>
                {project.user}
            </td>
            <td>
            <button onClick={()=>delete_project(project.id)} type='button'>Delete</button>
            </td>
        </tr>
)
}
const ProjectList = ({projects, delete_project}) => {
    return (
    <table>
        <th>
            id
        </th>
        <th>
            Name
        </th>
        <th>
            url_repo
        </th>
        <th>
            user
        </th>
        {projects.map((project) => <ProjectItem project={project} delete_project={delete_project}/>)}
    </table>
)
}
export default ProjectList