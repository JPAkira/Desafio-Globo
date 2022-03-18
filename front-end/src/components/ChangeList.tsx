import '../assets/Styles/ChangeList.css'
import {useState, ChangeEvent, useCallback, useEffect} from "react"
import axios from 'axios';

export function ChangeList() {
    const [nmposts, setNmPosts] = useState(4)
    const [posts, setPosts] = useState([{
        texto: String,
        tags: [{id:Number, name:String, card_id: Number}]
    }]);
    const [haveMore, setHaveMore] = useState(true);

    const getAllPosts = useCallback(async () => {
        axios.get('http://127.0.0.1:5000/cards')
        .then(response => {
            setPosts(response.data.cards)
            setHaveMore(response.data.cards.length - nmposts > 0)
        })
        .catch(error => console.log(error))
    }, [])
    useEffect(() => {
        getAllPosts()   
    }, [])
    

    const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.value) {
            axios.get('http://127.0.0.1:5000/cards/' + e.target.value)
            .then(response => {
                setPosts(response.data.cards)
                setHaveMore(posts.length - nmposts > 0)
            })
            .catch(error => console.log(error))
        }
        else {
            getAllPosts()
        }

      };
    function showMore() {
        setNmPosts(nmposts+4)
        setHaveMore(posts.length - nmposts > 0)
    }

    return (
        <div className="changelist">
            {posts.slice(0, nmposts).map (post => (
            <div className="card">
                <p><b>{post.texto}</b></p>
                {post.tags.map (tag => (<span><b>{tag.name}</b></span>))}
            </div>
            ))}
            <div className={haveMore ? "card-button-box showMore" : "card-button-box hideMore"}>
                <button onClick={showMore} className="card-ver-mais">Toque para exibir mais insights</button>
            </div>
            <div className="card-filtrar-box">
                <input onInput={handleInputChange} placeholder='Pesquise por termos ou categorias'></input>
            </div>
        </div>
    )
}