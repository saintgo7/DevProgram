class ResponseController < ApplicationController
  before_action :set_response, only: [:show, :edit, :update, :destroy]

  # GET /response
  def index
    @responses = Response.all
    render json: @responses
  end

  # GET /response/1
  def show
    render json: @response
  end

  # POST /response
  def create
    @response = Response.new(response_params)

    if @response.save
      render json: @response, status: :created
    else
      render json: @response.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /response/1
  def update
    if @response.update(response_params)
      render json: @response
    else
      render json: @response.errors, status: :unprocessable_entity
    end
  end

  # DELETE /response/1
  def destroy
    @response.destroy
    head :no_content
  end

  private

  def set_response
    @response = Response.find(params[:id])
  end

  def response_params
    params.require(:response).permit(:name)
  end
end
