import { useSearchParams } from "react-router-dom";

function MainPage() {
    const [searchPararams, setSearchParams] = useSearchParams();
    console.log(searchPararams.get('mode')); // null or dark
    return (
        <div className={['main', searchPararams.get('mode')].join(' ')}>
            <h1>Home</h1>
            <button onClick={() => {
                setSearchParams({mode: 'dark'});
            }}>Dark Mode</button>
        </div>
    );
}

export default MainPage;