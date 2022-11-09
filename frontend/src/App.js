import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import ToDoList from './components/ToDo.js'
import NotFound404 from './components/NotFound404.js'
import LoginForm from './components/Auth.js'
import MenuList from './components/Menu.js'
import Footer from './components/Footer.js'
import axios from 'axios'
import Cookies from 'universal-cookie';
import {BrowserRouter, Route, Routes, Link, useLocation, Navigate} from "react-router-dom"
import ProjectForm from './components/ProjectForm.js'
class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }
        create_project(name, users){
            const headers = this.get_headers()
            const data = {name:name, user:users}
            axios.post(`http://127.0.0.1:8000/api/project/`, data,  {headers}).then(response => {
                this.load_data()
            }).catch(error => {
                console.log(error)
                this.setState({projects:[]})})
        }

        get_headers() {
            let headers = {
            'Content-Type': 'application/json'
            }
            if (this.is_authenticated())
            {
            headers['Authorization'] = 'Token ' + this.state.token
            }
            return headers
    }
        get_token(username, password) {
            axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
            password: password})
            .then(response => {
            this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

        set_token(token) {
            const cookies = new Cookies()
            cookies.set('token', token)
            this.setState({'token': token}, ()=>this.load_data())
            }

        is_authenticated() {
            return this.state.token != ''
            }

        delete_project(id){
            const headers = this.get_headers()
            axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers}).then(response => {
                this.load_data()
            }).catch(error => {
                console.log(error)
                this.setState({projects:[]})})
        }

        logout() {
            this.set_token('')
            }

        get_token_from_storage() {
            const cookies = new Cookies()
            const token = cookies.get('token')
            this.setState({'token': token}, ()=>this.load_data())
            }

        load_data(){
            const headers = this.get_headers()
            axios.get('http://127.0.0.1:8000/api/userauth', {headers})
                .then(response => {
                    const users = response.data
                            this.setState(
                            {
                                'users': users
                            }
                    )
            }).catch(error => {console.log(error)
            this.setState({users: []})})

            axios.get('http://127.0.0.1:8000/api/project', {headers})
                .then(response => {
                    const projects = response.data
                            this.setState(
                            {
                                'projects': projects
                            }
                    )
            }).catch(error => {console.log(error)
            this.setState({projects: []})})

            axios.get('http://127.0.0.1:8000/api/todo', {headers})
                .then(response => {
                    const todos = response.data
                            this.setState(
                            {
                                'todos': todos
                            }
                    )
            }).catch(error => {console.log(error)
            this.setState({todos: []})})

    }


    componentDidMount() {
        this.get_token_from_storage()
        }
    render () {
    return (
        <div>
        <BrowserRouter>
            <nav>
                <li>
                    <Link to='/users/'>Users</Link>
                </li>
                <li>
                    <Link to='/projects/'>Projects</Link>
                </li>
                <li>
                    <Link to='/projects/create'>Projects create</Link>
                </li>
                <li>
                    <Link to='/todo/'>ToDoList</Link>
                </li>
                <li>
                    {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button>:<Link to='/login'>Login</Link>}
                </li>
            </nav>
            <Routes>
            {/*<Route exact path='/' element={<Navigate to='/users/'>}/>*/}
            {/*<p> <MenuList/> </p>*/}
            <Route exact path='users' element={<UserList
                users={this.state.users}/>}/>
            <Route exact path='projects' element={<ProjectList
                projects={this.state.projects} delete_project={(id)=>this.delete_project(id)} />}/>

            <Route exact path='projects/create'
                element={<ProjectForm users={this.state.users}
                    create_project={(name, user)=>this.create_project(name, user)} />}/>

            <Route exact path='todo' element={<ToDoList
                todos={this.state.todos}/>}/>
            <Route exact path='login' element={<LoginForm
                get_token={(username, password) => this.get_token(username, password)}/>}/>
            <Route exact path='*' element={<NotFound404/>}/>
            </Routes>
            </BrowserRouter>
            {/*<footer><Footer/></footer>*/}
        </div>
    )
}
}
export default App;