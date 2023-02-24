import React from 'react'
import {useParams} from "react-router-dom"

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
const ProjectSet = ({projects}) => {
    let {userId} useParams()
    let filter_projects = projects.filter((project) => project.users.includes(parseInt(userId))
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
        {filter_projects.map((project) => <ProjectItem project={project} />)}
    </table>
)
}
export default ProjectSet