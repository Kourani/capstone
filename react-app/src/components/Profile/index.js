
import react from 'react'

import {useSelector} from 'react-redux'

import "./Profile.css"


export default function Profile(){

    const userState = useSelector(state=>state.session)

    let date = new Date(userState.user.birthday)
    let day = date.getDate() 
    let month = date.getMonth()+1

    console.log(day, 'birthday')
    console.log(month, 'help')

    const today = new Date()

    console.log(today, '!!!!')
    let todayDay = today.getDate() 
    let todayMonth = today.getMonth()+1 

    console.log(todayDay, 'please')
    console.log(todayMonth, 'now')

    return (
        <div className='newProfile'>
            {todayDay === day && todayMonth === month ? `Happy Birthday! ${userState.user.firstName} ${userState.user.lastName}` : `Welcome Back ${userState.user.firstName} ${userState.user.lastName}` }
            <img className='tinyImage' src={userState.user.profileIcon} alt='Image'/>
        </div>
    )
}
