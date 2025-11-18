class InterceptorController < ApplicationController
  before_action :set_interceptor, only: [:show, :edit, :update, :destroy]

  # GET /interceptor
  def index
    @interceptors = Interceptor.all
    render json: @interceptors
  end

  # GET /interceptor/1
  def show
    render json: @interceptor
  end

  # POST /interceptor
  def create
    @interceptor = Interceptor.new(interceptor_params)

    if @interceptor.save
      render json: @interceptor, status: :created
    else
      render json: @interceptor.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /interceptor/1
  def update
    if @interceptor.update(interceptor_params)
      render json: @interceptor
    else
      render json: @interceptor.errors, status: :unprocessable_entity
    end
  end

  # DELETE /interceptor/1
  def destroy
    @interceptor.destroy
    head :no_content
  end

  private

  def set_interceptor
    @interceptor = Interceptor.find(params[:id])
  end

  def interceptor_params
    params.require(:interceptor).permit(:name)
  end
end
