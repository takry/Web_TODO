import React from 'react'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.url_repo}
            </td>
            <td>
                {project.user}
            </td>
        </tr>
)
}
const ProjectList = ({projects}) => {
    return (
    <table>
        <th>
            Name
        </th>
        <th>
            url_repo
        </th>
        <th>
            user
        </th>
        {projects.map((project) => <ProjectItem project={project} />)}
    </table>
)
}
export default ProjectList