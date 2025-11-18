class ContactController < ApplicationController
  before_action :set_contact, only: [:show, :edit, :update, :destroy]

  # GET /contact
  def index
    @contacts = Contact.all
    render json: @contacts
  end

  # GET /contact/1
  def show
    render json: @contact
  end

  # POST /contact
  def create
    @contact = Contact.new(contact_params)

    if @contact.save
      render json: @contact, status: :created
    else
      render json: @contact.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /contact/1
  def update
    if @contact.update(contact_params)
      render json: @contact
    else
      render json: @contact.errors, status: :unprocessable_entity
    end
  end

  # DELETE /contact/1
  def destroy
    @contact.destroy
    head :no_content
  end

  private

  def set_contact
    @contact = Contact.find(params[:id])
  end

  def contact_params
    params.require(:contact).permit(:name)
  end
end
