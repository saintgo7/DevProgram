class ErrorController < ApplicationController
  before_action :set_error, only: [:show, :edit, :update, :destroy]

  # GET /error
  def index
    @errors = Error.all
    render json: @errors
  end

  # GET /error/1
  def show
    render json: @error
  end

  # POST /error
  def create
    @error = Error.new(error_params)

    if @error.save
      render json: @error, status: :created
    else
      render json: @error.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /error/1
  def update
    if @error.update(error_params)
      render json: @error
    else
      render json: @error.errors, status: :unprocessable_entity
    end
  end

  # DELETE /error/1
  def destroy
    @error.destroy
    head :no_content
  end

  private

  def set_error
    @error = Error.find(params[:id])
  end

  def error_params
    params.require(:error).permit(:name)
  end
end
