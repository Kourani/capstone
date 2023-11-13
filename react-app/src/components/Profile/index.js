
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

    function balloons(){

        if (todayDay === day && todayMonth === month) {
            return(

                <>
               
                <div class="blns">
                    <p className='ballCenter'>Happy Birthday {userState.user.firstName} {userState.user.lastName}! </p>
                    
                    <div class="bln-1"></div>
                    <div class="bln-2"></div>
                    <div class="bln-3"></div>
                    <div class="bln-4"></div>
                    <div class="bln-5"></div>
                    <div class="bln-6"></div>
                    <div class="bln-7"></div>
                    <div class="bln-8"></div>
                    <div class="bln-9"></div>
                    <div class="bln-10"></div>
                    <div class="bln-11"></div>
                    <div class="bln-12"></div>
                    <div class="bln-13"></div>
                    <div class="bln-14"></div>
                    <div class="bln-15"></div>
                    <div class="bln-16"></div>
                    <div class="bln-17"></div>
                    <div class="bln-18"></div>
                    <div class="bln-19"></div>
                    <div class="bln-20"></div>
                </div>
                </>
            )
        }
        
        else {
            return (
                <>
                <div> Welcome Back {userState.user.firstName} {userState.user.lastName} </div>
                <img className='tinyImage' src={userState.user.profileIcon} alt='Image'/>
                </>
            )
        }
     
    }

    return (
        <>
        <div className='newProfile'>
            {balloons()}
        </div>
        </>
    )
}
