class WebSocketController < ApplicationController
  before_action :set_websocket, only: [:show, :edit, :update, :destroy]

  # GET /websocket
  def index
    @websockets = WebSocket.all
    render json: @websockets
  end

  # GET /websocket/1
  def show
    render json: @websocket
  end

  # POST /websocket
  def create
    @websocket = WebSocket.new(websocket_params)

    if @websocket.save
      render json: @websocket, status: :created
    else
      render json: @websocket.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /websocket/1
  def update
    if @websocket.update(websocket_params)
      render json: @websocket
    else
      render json: @websocket.errors, status: :unprocessable_entity
    end
  end

  # DELETE /websocket/1
  def destroy
    @websocket.destroy
    head :no_content
  end

  private

  def set_websocket
    @websocket = WebSocket.find(params[:id])
  end

  def websocket_params
    params.require(:websocket).permit(:name)
  end
end
