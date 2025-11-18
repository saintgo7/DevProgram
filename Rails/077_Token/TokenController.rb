class TokenController < ApplicationController
  before_action :set_token, only: [:show, :edit, :update, :destroy]

  # GET /token
  def index
    @tokens = Token.all
    render json: @tokens
  end

  # GET /token/1
  def show
    render json: @token
  end

  # POST /token
  def create
    @token = Token.new(token_params)

    if @token.save
      render json: @token, status: :created
    else
      render json: @token.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /token/1
  def update
    if @token.update(token_params)
      render json: @token
    else
      render json: @token.errors, status: :unprocessable_entity
    end
  end

  # DELETE /token/1
  def destroy
    @token.destroy
    head :no_content
  end

  private

  def set_token
    @token = Token.find(params[:id])
  end

  def token_params
    params.require(:token).permit(:name)
  end
end
