import React, {useState, useEffect, useRef} from 'react';
import axios from 'axios'
import filteredImage from './image/changed.jpg'
import zoomImage from './image/zoom.jpg'
//useRef


function App() {

    let reference  = useRef('')
    let refColor = useRef('')
    let refGamma = useRef(0)
    let refAlpha = useRef(0)
    let refChoice = useRef('')
    let reffX = useRef(0)
    let reffY = useRef(0)
    let refeX = useRef(0)
    let refeY = useRef(0)


    let [img, setImg] = useState(null);
    let [err, setError] = useState(true);
    let [errf, setErrorf] = useState(true);
    let [errc, setErrorc] = useState(true);
    let [errz, setErrorz] = useState(true);

    let [original, setImageStatus] = useState(true);


    function imageLoad(){
        setError(false);
        //setFile(reference.current.value)
        axios.get('http://127.0.0.1:5000/show/'+reference.current.value)
            .then(resp => {
                setImg(resp.data);
                setImg(`data:image/jpeg;base64,${resp.data.base64}`);



            })
            .catch(err => {
                setError(true);
            });
    }

    function setImageFilter(){
        setErrorf(false);
        setImageStatus(false);
        axios.post('http://127.0.0.1:5000/setFilter/'+refColor.current.value)
            .then(resp=> {
                console.log('filtered image upload');
            })
            .catch(err => {
                setErrorf(true);
            })
    }

    function setContrast(){
        setErrorc(false);
        setImageStatus(false);
        axios.post('http://127.0.0.1:5000/contrast/'+refAlpha.current.value+'/'+refGamma.current.value+'/'+refChoice.current.value)
            .then(resp=>{
                console.log(resp.data)
            })
            .catch(err =>{
                setErrorc(true);
            })
    }

    function zoom(){
        setErrorz(false);
        let file = ''
        if (original) file='original.jpg'
        else file = 'changed.jpg'
        axios.post('http://127.0.0.1:5000/zoom/'+file+'/'+reffX.current.value+'/'+reffY.current.value+'/'+refeX.current.value+'/'+refeY.current.value)
            .then(resp=>{
                console.log(resp.data)
            })
            .catch(err =>{
                setErrorz(true)
            })
    }


    return (
        <div>
            <textarea
                defaultValue={'image.jpg'}
                ref={reference}
            />
            <textarea
                defaultValue={'couleur'}
                ref={refColor}
            />
            <div>
                <textarea defaultValue={0.3} ref={refGamma} name={'gamma'}/>
                <textarea defaultValue={0.1} ref={refAlpha} name={'Alpha'}/>
                <textarea defaultValue={'neg'} ref={refChoice} name={'Choice'}/>
            </div>
            <div>
                <button onClick={e => imageLoad()} >Image</button>
                <button onClick={e => setContrast()} >Contrast</button>
                <button onClick={e => setImageFilter()} >Filtre</button>
                <button onClick={e=> setImageStatus(true)}>Undo</button>
            </div>

            { (!err && original) && (
                <img src={img} alt="Uploaded Image"/>
            )}
            { (!errf || !errc) && !original && (
                <img src={filteredImage} />
            )}


            {original && (<p>origine</p>)}
            {!original && (<p>filtrée</p>)}


            <div>
                <textarea defaultValue={0} ref={reffX} name={'firstx'}/>
                <textarea defaultValue={0} ref={reffY} name={'firsty'}/>
                <textarea defaultValue={100} ref={refeX} name={'endx'}/>
                <textarea defaultValue={100} ref={refeY} name={'endy'}/>
                <button onClick={e => zoom()} >Zoom</button>
            </div>
            { !errz && (
                <img src={zoomImage} />
            )}

        </div>


    );
}
export default App;