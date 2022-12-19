import React, { useEffect, useState } from 'react';

import * as UsuarioServer from './UsuarioServer';

const UsuarioList = () => {

    const [usuarios, setUsuarios] = useState([]);

    const listUsuarios = () => {
        try {
            const res = UsuarioServer.listUsuarios();
            console.log(res);

        } catch (error) {
            console.log(error);

        }
    };

    useEffect(() => {
        listUsuarios();
    }, []);

    return (
        <div>
            {usuarios.map((usuario) => (
                <h2>{usuario.name}</h2>
            ))}
        </div>
    )
};

export default UsuarioList;