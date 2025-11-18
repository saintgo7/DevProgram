class EmailController < ApplicationController
  before_action :set_email, only: [:show, :edit, :update, :destroy]

  # GET /email
  def index
    @emails = Email.all
    render json: @emails
  end

  # GET /email/1
  def show
    render json: @email
  end

  # POST /email
  def create
    @email = Email.new(email_params)

    if @email.save
      render json: @email, status: :created
    else
      render json: @email.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /email/1
  def update
    if @email.update(email_params)
      render json: @email
    else
      render json: @email.errors, status: :unprocessable_entity
    end
  end

  # DELETE /email/1
  def destroy
    @email.destroy
    head :no_content
  end

  private

  def set_email
    @email = Email.find(params[:id])
  end

  def email_params
    params.require(:email).permit(:name)
  end
end
