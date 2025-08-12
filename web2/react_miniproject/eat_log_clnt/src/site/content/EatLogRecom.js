import { useSelector } from "react-redux";
import NotLogin from "./sub_content/NotLogin";

const EatLogRecom = () => {
    const subscriber = useSelector((store) => store.AccountSlice);

    if (!subscriber.login) return <NotLogin />;
    else {
        return <div>EatLogRecom</div>;
    }
};

export default EatLogRecom;
