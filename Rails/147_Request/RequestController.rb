class RequestController < ApplicationController
  before_action :set_request, only: [:show, :edit, :update, :destroy]

  # GET /request
  def index
    @requests = Request.all
    render json: @requests
  end

  # GET /request/1
  def show
    render json: @request
  end

  # POST /request
  def create
    @request = Request.new(request_params)

    if @request.save
      render json: @request, status: :created
    else
      render json: @request.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /request/1
  def update
    if @request.update(request_params)
      render json: @request
    else
      render json: @request.errors, status: :unprocessable_entity
    end
  end

  # DELETE /request/1
  def destroy
    @request.destroy
    head :no_content
  end

  private

  def set_request
    @request = Request.find(params[:id])
  end

  def request_params
    params.require(:request).permit(:name)
  end
end
