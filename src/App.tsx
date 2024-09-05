import { useState } from 'react'

export default function App() {
  const [showBox,setBox]=useState<boolean>(false);
  const [showInput,setInput]=useState<boolean>(false);

  const handleBox=()=>{
    setBox(prev=>!prev)
  }

  console.log(showBox)
  
  return (
    <div>
      <div>
        <button
        id="btn-square-id"
        className='btn-square-class'
        name="btn-square-element"
        onClick={()=>handleBox()}
        >Show a square box
        </button>
        <div 
        className='div-square-class'
        id="div-square-id"
        
        style={{display:showBox ? "":"none",height:"50px",width:"50px",backgroundColor:"red"}}>Square Example</div>
        </div>

      <div>
      <button
      name="btn-display-input"
      id="btn-input-id"
      className='btn-input-class'
      onClick={()=>setInput(prev=>!prev)}
      >Display Text Input</button>
        <input 
        style={{display:showInput ? "":"none"}}
        name="input-element"
        placeholder='Type something'
        id="input-id"
        className='input-class'
        type="text"  
        >
        </input>
      </div>

      <div>
        <ul
        className='list-class'
        id="list-id"
        >
          <li><input type='checkbox'/>Show Square Box</li>
          <li><input type='checkbox'/>Show Square Box</li>
        </ul>
      </div>
    </div>
  )
}
