class SecurityController < ApplicationController
  before_action :set_security, only: [:show, :edit, :update, :destroy]

  # GET /security
  def index
    @securitys = Security.all
    render json: @securitys
  end

  # GET /security/1
  def show
    render json: @security
  end

  # POST /security
  def create
    @security = Security.new(security_params)

    if @security.save
      render json: @security, status: :created
    else
      render json: @security.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /security/1
  def update
    if @security.update(security_params)
      render json: @security
    else
      render json: @security.errors, status: :unprocessable_entity
    end
  end

  # DELETE /security/1
  def destroy
    @security.destroy
    head :no_content
  end

  private

  def set_security
    @security = Security.find(params[:id])
  end

  def security_params
    params.require(:security).permit(:name)
  end
end
