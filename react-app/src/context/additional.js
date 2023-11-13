

export function shoppingCart(){
    return(
        //  <i className="fas fa-shopping-cart fa-2x" ></i>
        <i className="fa-solid fa-bag-shopping fa-2x"></i>
    )
}

export function heart(){
    return (
        <i className="fas fa-heart"></i>
    )
}

export function plainHeart(){
    return (
        <i className="far fa-heart"></i>
    )
}

export function comingSoon(){
    return(
        window.alert('Coming Soon')
    )
}

export function futureWork(){
    return(
        <>
            <div>COMING SOON</div>
        </>
    )
}

export const monthNames = {
    1:'Janurary',
    2:'Febuary',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}

export default function empty(){
    return null
}
