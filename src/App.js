import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import FlipMove from "react-flip-move";
import { Table } from "react-bootstrap";
import Favicon from "react-favicon";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coinData: window.allCoinData,
      decentralizedClicks: 0,
      columnHeaders:    ["name", "symbol", "client_codebases", "consensus", 'consensus_distribution', "wealth_distribution", "rank", "consensus", "incentivized"],
      sortColumn: "name",
      sortAscending: false
    };
    this.dataUrl = "/data";
    if (process.env.NODE_ENV == "development") {
      this.dataUrl = "http://0.0.0.0:33507" + this.dataUrl;
    }
    window.r = this
  }

  decentClick = ()=>{
    if (this.state.decentralizedClicks < 6){

      this.setState({decentralizedClicks: this.state.decentralizedClicks + 2})
    } else {
      this.setState({decentralizedClicks: 0})
    }
  }
  sortBy = (sortColumn) =>{
    if (sortColumn == this.state.sortColumn) {
      return this.flipSortOrder()
    }
    const coinData = [...this.state.coinData];
    
    if (this.state.sortAscending) {
      coinData.sort((a, b) => a[sortColumn] >= b[sortColumn] ? 1 : -1);

    } else {
      coinData.sort((a, b) => b[sortColumn] >= a[sortColumn] ? 1 : -1);
    }
    this.setState({
      coinData,
      sortColumn
    });
    // this.setState({sortColumn})
  }
  flipSortOrder = () => {
    const { sortAscending, coinData } = this.state;
    const newCoinData = [...coinData]
    this.setState({
      sortAscending: !this.state.sortAscending,
      coinData: newCoinData.reverse()
    });
  };

  componentDidMount = () => {
    if (!window.allCoinData) {
      axios.get(this.dataUrl).then(d => {
        this.setState({
          coinData: d.data
        },()=>{
          this.sortBy('symbol')
        });
      });
      // 
      // window.setTimeout(()=>{

      // }, 2000)
    }
    window.r = this
  };
  renderDecentralized = ()=> {
    const decentralizedClicks = this.state.decentralizedClicks
    return <span> {"decentralized".split("").map((l, index)=>{
      
      return (index  >= 6 + decentralizedClicks) || (index  <= 6 - decentralizedClicks)   ? <span key={index}>{l}</span>:  <span  key={index}>&nbsp;</span>
    })} </span>
    return 
  }
  render() {
    const { coinData, columnHeaders } = this.state;

    return (
      <div className="App">
        <Favicon url="https://d30y9cdsu7xlg0.cloudfront.net/png/58197-200.png" />

        <nav id="navbar" className="navbar navbar-dark">
          <div id="nav-items-container">
            <div className="navbar-brand" onClick={this.decentClick}>
              <i className="fas fa-balance-scale" /> are we{" "}
              <span id="decentralized">{this.renderDecentralized()} yet? </span>
            </div>
            <div id="header-right-wrapper">
              <div>
                <a className="navbar-brand" href={this.dataUrl}>
                  <i className="fas fa-fw fa-code" /> JSON API
                </a>
              </div>
              <div>
                <a
                  className="navbar-brand"
                  href="https://github.com/DZGoldman/awdy"
                >
                  <i className="fab fa-fw fa-github" /> Contribute on Github
                </a>
              </div>
            </div>
          </div>
        </nav>

        <Table className="table table-striped">
          <thead>
          <tr   id='header-row'>
              {columnHeaders.map( (h, i) => {
                const isCurrentColumn =     h == this.state.sortColumn;
                return (
                  <th
                    key={h}
                    onClick={() => this.sortBy(h)}
                    className={
                      isCurrentColumn
                        ? "emphasized-col"
                        : "deemphasized-col"
                    }
                  >
                    <span>
                    {this.state.columnHeaders[i]}
                    {isCurrentColumn && (!this.state.sortAscending ? <span className='arrow'>&#x2191;</span> :  <span className='arrow'>&#x2193;</span>)}</span>
             
                  </th>
                );
              })}
            </tr>
          </thead>
          <tbody>
            {/* <FlipMove> */}
            {coinData && coinData.length > 0 && coinData.map((coin, index) => {
              return (
                <tr key={coin.symbol}>
                {/* columnHeaders:    ["name", "symbol", "client_codebases", "consensus", 'consensus_distribution', "rank"], */}

                  <td><a target ='_blank' href={ coin.homepage}>{coin.name}</a></td>
                  <td>{coin.symbol}</td>
                  <td>{coin.client_codebases}</td>
                  <td>{coin.consensus}</td>
                  <td>{coin.consensus_distribution}</td>
                  <td>{coin.wealth_distribution}</td>
                  <td>{coin.rank}</td>
                  <td>{coin.consensus}</td>
                  <td>{coin.incentivized}</td>
                 
          
                  
                </tr>
              );
            })}
            {/* </FlipMove> */}
          </tbody>
        </Table>

        <footer>
          <div className="footer" id="footer">
            <div className="footer-bottom">
              <div className="footer-row">
                <div>Created by Daniel Goldman </div>
                <div>
                  {" "}
                  <a target="_blank" href="https://twitter.com/DZack23">
                    {" "}
                    <i className="fab fa-twitter"> </i>{" "}
                  </a>{" "}
                </div>
                <div>
                  {" "}
                  <a target="_blank" href="https://github.com/DZGoldman">
                    {" "}
                    <i className="fab fa-github" />{" "}
                  </a>{" "}
                </div>
                <div>
                  {" "}
                  <a target="_blank" href="https://medium.com/@dzack23">
                    {" "}
                    <i className="fab fa-medium" />{" "}
                  </a>{" "}
                </div>
                <div>
                  {" "}
                  <a target="_blank" href="http://danielzgoldman.com/">
                    {" "}
                    <i className="fa fa-home" />{" "}
                  </a>{" "}
                </div>
              </div>
              <div id="inspired-by" className="footer-row">
                {" "}
                blatantly inspired by &nbsp;
                <a target="_blank" href="https://arewedecentralizedyet.com/">
                  arewedecentralizedyet.com
                </a>
              </div>

              <div id="tips" className="footer-row">
                <div>
                  {" "}
                  <p>
                    {" "}
                    Help promote wealth decentralization by giving me yours:
                  </p>{" "}
                </div>
                <div className="tip">
                  BTC: <b>33STRJgjFgG2r8vEy9xLKN5dYfw26tSmVi</b>
                </div>
                <div className="tip">
                  ETH/DAI: <b>0x36de2576CC8CCc79557092d4Caf47876D3fd416c</b>
                </div>
                <div className="tip">
                  XMR:{" "}
                  <b>
                    832DjfVp9ddVwQqq9hvXoHYfRL5f2kyRwDWFBaRdX3151sbp1VNvy5PdTRphnaa4RqGqJFRQfsHdnaPbtyfzQ6jKGtvJdPR
                  </b>
                </div>
              </div>
            </div>
          </div>
        </footer>
      </div>
    );
  }
}

export default App;
