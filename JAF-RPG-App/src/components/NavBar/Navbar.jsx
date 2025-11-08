import { Link } from "react-router";

const Navbar = () => {
    return (
        <nav>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/characters">Characters</Link>
            </li>
            <li>
                <Link to="/locations">Locations</Link>
            </li>
            <li>
                <Link to="/patchnotes">Patch Notes</Link>
            </li>
            <li>
                <Link to="/login">Login</Link>
            </li>
            <li>
                <Link to ="/sign-up">Create Account</Link>
            </li>            
        </nav>
    );
};

export default Navbar;