//
// blocking_udp_echo_client.cpp
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
// Copyright (c) 2003-2017 Christopher M. Kohlhoff (chris at kohlhoff dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//

#include <cstdlib>
#include <cstring>
#include <iostream>
#include <boost/asio.hpp>
#include <thread>
#include <chrono>
#include <random>


using boost::asio::ip::udp;

enum { max_length = 200 };

int main(int argc, char* argv[])
{
  try
  {
    if (argc != 5)
    {
      std::cerr << "Usage: blocking_udp_echo_client <host> <port> <latency_ms> <num_repetitions>\n";
      return 1;
    }

    boost::asio::io_service io_context;

    udp::socket s(io_context, udp::endpoint(udp::v4(), 0));

    udp::resolver resolver(io_context);
    udp::endpoint endpoint = *resolver.resolve({udp::v4(), argv[1], argv[2]});
    const int latency_ms = atoi(argv[3]);
    const int num_rep = atoi(argv[4]);

    std::random_device rd{};
    std::mt19937 gen{rd()};
    std::normal_distribution<> d{latency_ms,5};

    char request[max_length] = "Message from RPI";
    size_t request_length = max_length; 
    for(int i = 0; i < num_rep; ++i){
      s.send_to(boost::asio::buffer(request, request_length), endpoint);
      const int val = d(gen); 
      std::cout << "Val generated =  " << val << std::endl; 
      std::this_thread::sleep_for(std::chrono::milliseconds(val));
    }
  }
  catch (std::exception& e)
  {
    std::cerr << "Exception: " << e.what() << "\n";
  }

  return 0;
}

