class MessageController < ApplicationController
  before_action :set_message, only: [:show, :edit, :update, :destroy]

  # GET /message
  def index
    @messages = Message.all
    render json: @messages
  end

  # GET /message/1
  def show
    render json: @message
  end

  # POST /message
  def create
    @message = Message.new(message_params)

    if @message.save
      render json: @message, status: :created
    else
      render json: @message.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /message/1
  def update
    if @message.update(message_params)
      render json: @message
    else
      render json: @message.errors, status: :unprocessable_entity
    end
  end

  # DELETE /message/1
  def destroy
    @message.destroy
    head :no_content
  end

  private

  def set_message
    @message = Message.find(params[:id])
  end

  def message_params
    params.require(:message).permit(:name)
  end
end
