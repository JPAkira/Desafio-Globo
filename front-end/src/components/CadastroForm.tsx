import '../assets/Styles/CadastroForm.css'
import axios from "axios";

export function CadastroForm() {
    function addNewUser() {
        let texto = (document.getElementById("texto") as HTMLInputElement).value
        let tags = (document.getElementById("tags") as HTMLInputElement).value
        let tags_list = tags.split(',')
        
        const newCard = {
            texto: texto,
            tags: tags_list
        }   
    
        axios.post('http://127.0.0.1:5000/card', newCard)
        .then(response => {
            console.log('Sucess')
            alert(JSON.stringify(response.data))
        })
        .catch(error => console.log(error))
    }
    return (
        <div className='form-box'>
            <form onSubmit={addNewUser} >
            <label>Insights</label>
            <textarea id='texto'></textarea>
            <label>Tags</label>
            <input id='tags' placeholder='tag1, tag2, tag3'></input>
            <input type='submit' value='Salvar'></input>
            </form>
        </div>
    )
}