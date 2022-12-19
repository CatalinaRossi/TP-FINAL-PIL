const API_URL = 'http://127.0.0.1:8000/api/usuarios/';


export const listUsuarios = async () => {
    return await fetch(API_URL);
}